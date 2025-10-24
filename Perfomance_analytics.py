import pandas as pd
import numpy as np
import heapq
import os
import matplotlib.pyplot as plt
import seaborn as sns


class PerformanceAnalytics:
    def __init__(self, csv_file=r"D:\projects\School management\sampledata\perfomance.csv"):
        self.csv_file = csv_file
        self.data = None
        self.subjects = []
        self.load_from_csv()

    # ---------------- LOAD DATA ----------------
    def load_from_csv(self):
        """Load student performance data."""
        if not os.path.exists(self.csv_file):
            print(f"⚠️ File '{self.csv_file}' not found.")
            return

        self.data = pd.read_csv(self.csv_file, sep="\t|,", engine="python")
        self.subjects = list(self.data.columns[2:])  # skip student_id and name
        print(f"✅ Loaded performance data for {len(self.data)} students across {len(self.subjects)} subjects.")

    # ---------------- MATRIX OPERATIONS ----------------
    def get_score_matrix(self):
        """Return matrix of student scores."""
        matrix = self.data[self.subjects].to_numpy()
        print("\n🎯 Score Matrix:")
        print(matrix)
        return matrix

    def average_per_subject(self):
        """Compute average score per subject."""
        print("\n📊 Average Score per Subject:")
        for subject in self.subjects:
            avg = self.data[subject].mean()
            print(f"{subject:<10}: {avg:.2f}")

    def overall_average_per_student(self):
        """Compute overall average score per student."""
        self.data["Average"] = self.data[self.subjects].mean(axis=1)
        print("\n📈 Overall Average per Student:")
        for _, row in self.data.iterrows():
            print(f"{row['name']:<10}: {row['Average']:.2f}")
        return self.data

    # ---------------- HEAP FOR TOP PERFORMERS ----------------
    def top_performers(self, n=3):
        """Find top N students using a max heap."""
        if "Average" not in self.data.columns:
            self.overall_average_per_student()

        heap = []
        for _, row in self.data.iterrows():
            heapq.heappush(heap, (-row["Average"], row["student_id"], row["name"]))

        print(f"\n🏆 Top {n} Performers:")
        for i in range(min(n, len(heap))):
            avg, sid, name = heapq.heappop(heap)
            print(f"{i+1}. {name:<10} (ID: {sid}) — Average: {-avg:.2f}")

    # ---------------- GRAPH / CORRELATION ----------------
    def correlation_graph(self):
        """Show correlation matrix between subjects."""
        corr = self.data[self.subjects].corr()
        print("\n🔗 Subject Correlation Matrix:")
        print(corr)

        plt.figure(figsize=(6, 4))
        sns.heatmap(corr, annot=True, cmap="coolwarm", linewidths=0.5)
        plt.title("Subject Correlation Heatmap")
        plt.show()
        return corr

    # ---------------- VISUALIZATION ----------------
    def bar_chart_top_students(self):
        """Bar chart of students ranked by average score."""
        if "Average" not in self.data.columns:
            self.overall_average_per_student()

        sorted_data = self.data.sort_values(by="Average", ascending=False)
        plt.figure(figsize=(7, 4))
        sns.barplot(x="name", y="Average", data=sorted_data, palette="viridis")
        plt.title("Top Student Performance")
        plt.ylabel("Average Score")
        plt.xlabel("Student")
        plt.show()


# ---------------- TEST SECTION ----------------
if __name__ == "__main__":
    analyzer = PerformanceAnalytics(r"D:\projects\School management\sampledata\perfomance.csv")

    analyzer.get_score_matrix()
    analyzer.average_per_subject()
    analyzer.overall_average_per_student()
    analyzer.top_performers(3)
    analyzer.correlation_graph()
    analyzer.bar_chart_top_students()
