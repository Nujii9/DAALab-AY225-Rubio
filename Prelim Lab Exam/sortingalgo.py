import csv
import time
import sys

# Increase recursion depth to handle Merge Sort on 100k rows
sys.setrecursionlimit(200000)

class SortingTool:
    def __init__(self, filename):
        self.filename = filename
        self.data = []
        self.load_time = 0

    def load_data(self):
        """
        Reads the CSV file and parses it into a list of dictionaries.
        """
        print(f"Reading file '{self.filename}'...")
        start_time = time.time()
        try:
            with open(self.filename, mode='r', newline='', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                # Clean header names
                reader.fieldnames = [name.strip() for name in reader.fieldnames]
                
                for row in reader:
                    # Convert ID to integer for proper numerical comparison
                    if 'ID' in row:
                        row['ID'] = int(row['ID'])
                    self.data.append(row)
                    
        except FileNotFoundError:
            print("Error: 'generated_data.csv' not found.")
            return
        
        end_time = time.time()
        self.load_time = end_time - start_time
        print(f"Successfully loaded {len(self.data)} records in {self.load_time:.4f} seconds.")

    def compare(self, val1, val2, reverse):
        """
        Comparison helper.
        """
        if reverse:
            return val1 < val2 # Descending
        return val1 > val2     # Ascending

    def bubble_sort(self, data, key, reverse=False):
        arr = data.copy()
        n = len(arr)
        for i in range(n):
            swapped = False
            for j in range(0, n - i - 1):
                val1 = arr[j][key]
                val2 = arr[j+1][key]
                
                if self.compare(val1, val2, reverse):
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    swapped = True
            if not swapped:
                break
        return arr

    def insertion_sort(self, data, key, reverse=False):
        arr = data.copy()
        for i in range(1, len(arr)):
            key_item = arr[i] 
            val_key = key_item[key]
            j = i - 1
            
            while j >= 0 and self.compare(arr[j][key], val_key, reverse):
                arr[j + 1] = arr[j] 
                j -= 1
            arr[j + 1] = key_item
        return arr

    def merge_sort(self, data, key, reverse=False):
        if len(data) <= 1:
            return data
        
        mid = len(data) // 2
        left = self.merge_sort(data[:mid], key, reverse)
        right = self.merge_sort(data[mid:], key, reverse)
        
        return self.merge(left, right, key, reverse)

    def merge(self, left, right, key, reverse):
        sorted_list = []
        i = j = 0
        
        while i < len(left) and j < len(right):
            val1 = left[i][key]
            val2 = right[j][key]
            
            pick_left = False
            if reverse:
                if val1 > val2: pick_left = True
            else:
                if val1 < val2: pick_left = True
            
            if pick_left:
                sorted_list.append(left[i])
                i += 1
            else:
                sorted_list.append(right[j])
                j += 1
                
        sorted_list.extend(left[i:])
        sorted_list.extend(right[j:])
        return sorted_list

    def run(self):
        self.load_data()
        if not self.data:
            return

        while True:
            print("\n" + "="*50)
            print("       SORTING BENCHMARK TOOL")
            print("="*50)

            # --- Step 1: Number of Rows ---
            print(f"Total Records Available: {len(self.data)}")
            n_str = input(f"How many rows to sort? (Press Enter for ALL {len(self.data)}): ")
            
            if n_str.strip() == "":
                n = len(self.data)
            else:
                try:
                    n = int(n_str)
                    if n > len(self.data): n = len(self.data)
                except ValueError:
                    print("Invalid input. Defaulting to 1000.")
                    n = 1000

            subset = self.data[:n]

            # --- Step 2: Column Selection ---
            print("\nSelect Column:")
            print("[1] ID")
            print("[2] FirstName")
            print("[3] LastName")
            col_map = {'1': 'ID', '2': 'FirstName', '3': 'LastName'}
            choice = input("Selection (1-3): ")
            key = col_map.get(choice, 'ID')

            # --- Step 3: Order Selection ---
            print("\nSelect Order:")
            print("[1] Ascending (A-Z)")
            print("[2] Descending (Z-A)")
            order_choice = input("Selection (1-2): ")
            reverse = True if order_choice == '2' else False
            order_str = "Descending" if reverse else "Ascending"

            # --- Step 4: Algorithm Selection ---
            print("\nSelect Algorithm:")
            print("[1] Bubble Sort")
            print("[2] Insertion Sort")
            print("[3] Merge Sort")
            algo_choice = input("Selection (1-3): ")

            # Safety Warning
            if n > 10000 and algo_choice in ['1', '2']:
                print(f"\n[WARNING] Sorting {n} records with Bubble/Insertion sort will take a LONG time.")
                confirm = input("Are you sure you want to continue? (y/n): ")
                if confirm.lower() != 'y':
                    continue

            # --- Execution ---
            print(f"\nRunning Sort on {n} rows by {key} ({order_str})...")
            start_time = time.time()
            
            sorted_data = []
            algo_name = ""
            
            if algo_choice == '1':
                algo_name = "Bubble Sort"
                sorted_data = self.bubble_sort(subset, key, reverse)
            elif algo_choice == '2':
                algo_name = "Insertion Sort"
                sorted_data = self.insertion_sort(subset, key, reverse)
            elif algo_choice == '3':
                algo_name = "Merge Sort"
                sorted_data = self.merge_sort(subset, key, reverse)
            else:
                print("Invalid algorithm.")
                continue

            sort_duration = time.time() - start_time

            # --- PRINTING DATASET ---
            print("\n" + "="*50)
            print(f"SORTED DATASET ({len(sorted_data)} Records)")
            print("="*50)
            print(f"{'ID':<15} {'FirstName':<15} {'LastName':<15}")
            print("-" * 45)
            
            # Print ALL records based on input N
            for row in sorted_data:
                print(f"{row['ID']:<15} {row['FirstName']:<15} {row['LastName']:<15}")
            print("-" * 45)
            
            # --- PRINTING BENCHMARK TIME (AT THE END) ---
            print("\n" + "#"*50)
            print(f"   BENCHMARK RESULTS: {algo_name}")
            print("#"*50)
            print(f"Records Processed: {n}")
            print(f"Load Time:         {self.load_time:.6f} seconds")
            print(f"Sort Time:         {sort_duration:.6f} seconds")
            print("#"*50)

            if input("\nRun another test? (y/n): ").lower() != 'y':
                break

if __name__ == "__main__":
    tool = SortingTool('generated_data.csv')
    tool.run()