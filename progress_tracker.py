#!/usr/bin/env python3
"""
Progress Tracker for NeetCode 250 Problems
Helps you track your progress across different problem categories
"""

import os
import json
from datetime import datetime

class ProgressTracker:
    def __init__(self):
        self.categories = {
            'arrays_strings': {'name': 'Arrays & Strings', 'problems': [], 'completed': 0},
            'linked_lists': {'name': 'Linked Lists', 'problems': [], 'completed': 0},
            'trees': {'name': 'Trees & Binary Trees', 'problems': [], 'completed': 0},
            'graphs': {'name': 'Graphs & Traversals', 'problems': [], 'completed': 0},
            'dp': {'name': 'Dynamic Programming', 'problems': [], 'completed': 0},
            'sliding_window': {'name': 'Sliding Window', 'problems': [], 'completed': 0},
            'binary_search': {'name': 'Binary Search', 'problems': [], 'completed': 0},
            'backtracking': {'name': 'Backtracking', 'problems': [], 'completed': 0},
            'stack_queue': {'name': 'Stack & Queues', 'problems': [], 'completed': 0},
            'heap_greedy': {'name': 'Heap & Greedy', 'problems': [], 'completed': 0},
            'bit_manipulation': {'name': 'Bit Manipulation', 'problems': [], 'completed': 0},
            'math_logic': {'name': 'Math & Logic', 'problems': [], 'completed': 0},
            'others': {'name': 'Others & Miscellaneous', 'problems': [], 'completed': 0}
        }
        self.progress_file = 'progress.json'
        self.load_progress()
    
    def load_progress(self):
        """Load existing progress from file"""
        if os.path.exists(self.progress_file):
            try:
                with open(self.progress_file, 'r') as f:
                    data = json.load(f)
                    for category, info in data.items():
                        if category in self.categories:
                            self.categories[category].update(info)
            except:
                print("Could not load progress file. Starting fresh.")
    
    def save_progress(self):
        """Save current progress to file"""
        with open(self.progress_file, 'w') as f:
            json.dump(self.categories, f, indent=2)
    
    def add_problem(self, category, problem_name, difficulty='Medium', completed=False):
        """Add a problem to a category"""
        if category not in self.categories:
            print(f"Invalid category: {category}")
            return
        
        problem = {
            'name': problem_name,
            'difficulty': difficulty,
            'completed': completed,
            'date_added': datetime.now().strftime('%Y-%m-%d'),
            'date_completed': datetime.now().strftime('%Y-%m-%d') if completed else None
        }
        
        self.categories[category]['problems'].append(problem)
        if completed:
            self.categories[category]['completed'] += 1
        self.save_progress()
    
    def mark_completed(self, category, problem_name):
        """Mark a problem as completed"""
        if category not in self.categories:
            print(f"Invalid category: {category}")
            return
        
        for problem in self.categories[category]['problems']:
            if problem['name'] == problem_name:
                if not problem['completed']:
                    problem['completed'] = True
                    problem['date_completed'] = datetime.now().strftime('%Y-%m-%d')
                    self.categories[category]['completed'] += 1
                    self.save_progress()
                    print(f"✅ Marked '{problem_name}' as completed!")
                else:
                    print(f"Problem '{problem_name}' is already completed.")
                return
        
        print(f"Problem '{problem_name}' not found in {category}.")
    
    def show_progress(self):
        """Display current progress"""
        print("\n" + "="*60)
        print("📊 NEEETCODE 250 PROGRESS TRACKER")
        print("="*60)
        
        total_problems = 0
        total_completed = 0
        
        for category, info in self.categories.items():
            problems_count = len(info['problems'])
            completed_count = info['completed']
            total_problems += problems_count
            total_completed += completed_count
            
            progress_bar = self._create_progress_bar(completed_count, problems_count)
            
            print(f"\n📁 {info['name']}")
            print(f"   Progress: {completed_count}/{problems_count} ({progress_bar})")
            
            if problems_count > 0:
                percentage = (completed_count / problems_count) * 100
                print(f"   Completion: {percentage:.1f}%")
        
        print("\n" + "="*60)
        overall_percentage = (total_completed / total_problems * 100) if total_problems > 0 else 0
        print(f"🎯 OVERALL PROGRESS: {total_completed}/{total_problems} ({overall_percentage:.1f}%)")
        print("="*60)
    
    def _create_progress_bar(self, completed, total, width=20):
        """Create a visual progress bar"""
        if total == 0:
            return "░" * width
        
        filled = int((completed / total) * width)
        bar = "█" * filled + "░" * (width - filled)
        return bar
    
    def list_problems(self, category):
        """List all problems in a category"""
        if category not in self.categories:
            print(f"Invalid category: {category}")
            return
        
        info = self.categories[category]
        print(f"\n📁 {info['name']} Problems:")
        print("-" * 40)
        
        if not info['problems']:
            print("No problems added yet.")
            return
        
        for i, problem in enumerate(info['problems'], 1):
            status = "✅" if problem['completed'] else "⏳"
            print(f"{i:2d}. {status} {problem['name']} ({problem['difficulty']})")
    
    def get_next_problem(self, category):
        """Get the next uncompleted problem in a category"""
        if category not in self.categories:
            print(f"Invalid category: {category}")
            return None
        
        for problem in self.categories[category]['problems']:
            if not problem['completed']:
                return problem
        
        print(f"No uncompleted problems in {category}.")
        return None

def main():
    tracker = ProgressTracker()
    
    while True:
        print("\n" + "="*50)
        print("🧠 NEEETCODE 250 PROGRESS TRACKER")
        print("="*50)
        print("1. Show Progress")
        print("2. Add Problem")
        print("3. Mark Problem Complete")
        print("4. List Problems by Category")
        print("5. Get Next Problem")
        print("6. Exit")
        
        choice = input("\nEnter your choice (1-6): ").strip()
        
        if choice == '1':
            tracker.show_progress()
        
        elif choice == '2':
            print("\nAvailable categories:")
            for i, (cat, info) in enumerate(tracker.categories.items(), 1):
                print(f"{i}. {info['name']} ({cat})")
            
            cat_choice = input("Enter category number: ").strip()
            try:
                cat_index = int(cat_choice) - 1
                category = list(tracker.categories.keys())[cat_index]
            except:
                print("Invalid choice.")
                continue
            
            problem_name = input("Enter problem name: ").strip()
            difficulty = input("Enter difficulty (Easy/Medium/Hard): ").strip()
            completed = input("Is it completed? (y/n): ").strip().lower() == 'y'
            
            tracker.add_problem(category, problem_name, difficulty, completed)
            print("✅ Problem added successfully!")
        
        elif choice == '3':
            print("\nAvailable categories:")
            for i, (cat, info) in enumerate(tracker.categories.items(), 1):
                print(f"{i}. {info['name']} ({cat})")
            
            cat_choice = input("Enter category number: ").strip()
            try:
                cat_index = int(cat_choice) - 1
                category = list(tracker.categories.keys())[cat_index]
            except:
                print("Invalid choice.")
                continue
            
            tracker.list_problems(category)
            problem_name = input("Enter problem name to mark complete: ").strip()
            tracker.mark_completed(category, problem_name)
        
        elif choice == '4':
            print("\nAvailable categories:")
            for i, (cat, info) in enumerate(tracker.categories.items(), 1):
                print(f"{i}. {info['name']} ({cat})")
            
            cat_choice = input("Enter category number: ").strip()
            try:
                cat_index = int(cat_choice) - 1
                category = list(tracker.categories.keys())[cat_index]
            except:
                print("Invalid choice.")
                continue
            
            tracker.list_problems(category)
        
        elif choice == '5':
            print("\nAvailable categories:")
            for i, (cat, info) in enumerate(tracker.categories.items(), 1):
                print(f"{i}. {info['name']} ({cat})")
            
            cat_choice = input("Enter category number: ").strip()
            try:
                cat_index = int(cat_choice) - 1
                category = list(tracker.categories.keys())[cat_index]
            except:
                print("Invalid choice.")
                continue
            
            problem = tracker.get_next_problem(category)
            if problem:
                print(f"\n🎯 Next problem: {problem['name']} ({problem['difficulty']})")
        
        elif choice == '6':
            print("👋 Good luck with your coding journey!")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main() 