import csv
import os

class FeeRecord:
    def __init__(self, student_id, name, amount_paid, total_fee):
        self.student_id = int(student_id)
        self.name = name
        self.amount_paid = float(amount_paid)
        self.total_fee = float(total_fee)

    def balance(self):
        return self.total_fee - self.amount_paid


class Node:
    def __init__(self, record):
        self.record = record
        self.left = None
        self.right = None


class FeeBST:
    def __init__(self, csv_file=r"D:\projects\School management\sampledata\fees.csv"):
        self.root = None
        self.csv_file = csv_file
        self.load_from_csv()

    # ----------------- CSV HANDLING -----------------
    def load_from_csv(self):
        """Loads fee records from CSV into the BST."""
        if not os.path.exists(self.csv_file):
            print(f"⚠️ File '{self.csv_file}' not found. Starting with empty records.")
            return

        with open(self.csv_file, newline='', encoding='utf-8-sig') as file:
            reader = csv.DictReader(file)
            for row in reader:
                record = FeeRecord(
                    row['student_id'],
                    row['name'],
                    row['amount_paid'],
                    row['total_fee']
                )
                self.insert(record)
        print(f"✅ Loaded fee records from {self.csv_file}.")

    def save_to_csv(self):
        """Saves all records (in sorted order) back to CSV."""
        records = self.inorder()
        with open(self.csv_file, 'w', newline='', encoding='utf-8') as file:
            fieldnames = ['student_id', 'name', 'amount_paid', 'total_fee']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for r in records:
                student_id, name, amount_paid, total_fee, _ = r
                writer.writerow({
                    'student_id': student_id,
                    'name': name,
                    'amount_paid': amount_paid,
                    'total_fee': total_fee
                })
        print(f"💾 Fee records saved to {self.csv_file}.")

    # ----------------- BST OPERATIONS -----------------
    def insert(self, record):
        """Insert a new fee record into the BST."""
        if self.root is None:
            self.root = Node(record)
        else:
            self._insert(self.root, record)

    def _insert(self, current, record):
        if record.student_id < current.record.student_id:
            if current.left is None:
                current.left = Node(record)
            else:
                self._insert(current.left, record)
        elif record.student_id > current.record.student_id:
            if current.right is None:
                current.right = Node(record)
            else:
                self._insert(current.right, record)
        else:
            print(f"⚠️ Student {record.student_id} already exists!")

    def search(self, student_id):
        """Search for a record by student ID."""
        return self._search(self.root, student_id)

    def _search(self, current, student_id):
        if current is None:
            return None
        if current.record.student_id == student_id:
            return current.record
        elif student_id < current.record.student_id:
            return self._search(current.left, student_id)
        else:
            return self._search(current.right, student_id)

    def inorder(self):
        """Return all records sorted by student ID."""
        result = []
        self._inorder(self.root, result)
        return result

    def _inorder(self, node, result):
        if node:
            self._inorder(node.left, result)
            result.append((
                node.record.student_id,
                node.record.name,
                node.record.amount_paid,
                node.record.total_fee,
                node.record.balance()
            ))
            self._inorder(node.right, result)

    # ----------------- REPORT DISPLAY -----------------
    def display_fees(self):
        """Display fee payment summary for all students."""
        print("\n--- Fee Report ---")
        for sid, name, paid, total, balance in self.inorder():
            status = "✅ Cleared" if balance == 0 else f"💰 Balance: {balance}"
            print(f"{sid:<5} {name:<10} Paid: {paid:<8} Total: {total:<8} {status}")


# ----------------- TESTING SECTION -----------------
if __name__ == "__main__":
    tree = FeeBST(r"D:\projects\School management\sampledata\fees.csv")

    tree.display_fees()

    # Search for a student
    student_id = 103
    rec = tree.search(student_id)
    if rec:
        print(f"\nFound: {rec.name}, Paid: {rec.amount_paid}, Balance: {rec.balance()}")
    else:
        print(f"\n⚠️ Student ID {student_id} not found.")

    # Add new record (example)
    new_record = FeeRecord(106, "Faith", 5000, 10000)
    tree.insert(new_record)
    tree.save_to_csv()
    print("\n✅ Added new record and saved to CSV.")
    tree.display_fees()





