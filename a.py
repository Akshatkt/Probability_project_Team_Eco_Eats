import random
import matplotlib.pyplot as plt
from prettytable import PrettyTable
from tabulate import tabulate 
import statistics
import seaborn as sns

def create_sample_menu():
    menu = {
        "Day 1": {
            "Breakfast": {
                "Aloo Paratha with Dahi (Yogurt)": {"Total Prepared": 160, "Consumed": 50},
                "Poha (Flattened Rice) with Tea": {"Total Prepared": 35, "Consumed": 30},
                "Upma (Semolina Dish) with Coconut Chutney": {"Total Prepared": 30, "Consumed": 5}
            },
            "Lunch": {
                "Rajma (Kidney Beans) with Jeera Rice": {"Total Prepared": 70, "Consumed": 60},
                "Paneer Tikka with Naan": {"Total Prepared": 50, "Consumed": 40},
                "Mixed Vegetable Curry with Roti": {"Total Prepared": 50, "Consumed": 10}
            },
            "Snacks": {
                "Samosa with Green Chutney": {"Total Prepared": 20, "Consumed": 19},
                "Chai (Tea) with Pakoras": {"Total Prepared": 25, "Consumed": 15},
                "Bhel Puri": {"Total Prepared": 30, "Consumed": 15}
            },
            "Dinner": {
                "Chicken Biryani": {"Total Prepared": 60, "Consumed": 55},
                "Dal Tadka with Steamed Rice": {"Total Prepared": 40, "Consumed": 25},
                "Vegetable Pulao with Raita": {"Total Prepared": 55, "Consumed": 20}
            }
        },
        "Day 2": {
            "Breakfast": {
                "Idli with Sambhar and Coconut Chutney": {"Total Prepared": 45, "Consumed": 30},
                "Aloo Poori with Pickle": {"Total Prepared": 35, "Consumed": 30},
                "Mango Lassi": {"Total Prepared": 30, "Consumed": 20}
            },
            "Lunch": {
                "Palak Paneer with Roti": {"Total Prepared": 55, "Consumed": 50},
                "Tandoori Chicken with Naan": {"Total Prepared": 50, "Consumed": 48},
                "Masoor Dal with Jeera Rice": {"Total Prepared": 40, "Consumed": 15}
            },
            "Snacks": {
                "Dahi Puri": {"Total Prepared": 40, "Consumed": 25},
                "Gulab Jamun": {"Total Prepared": 15, "Consumed": 14},
                "Chai (Tea) with Biscuits": {"Total Prepared": 30, "Consumed": 15}
            },
            "Dinner": {
                "Mutton Rogan Josh with Pulao": {"Total Prepared": 65, "Consumed": 60},
                "Chole (Chickpea Curry) with Bhature": {"Total Prepared": 45, "Consumed": 40},
                "Mixed Vegetable Fried Rice": {"Total Prepared": 50, "Consumed": 45}
            }
        },
        "Day 3": {
            "Breakfast": {
                "Masala Dosa with Coconut Chutney": {"Total Prepared": 50, "Consumed": 45},
                "Aloo Paratha with Lassi": {"Total Prepared": 60, "Consumed": 55},
                "Medu Vada with Sambhar": {"Total Prepared": 40, "Consumed": 35}
            },
            "Lunch": {
                "Butter Chicken with Naan": {"Total Prepared": 60, "Consumed": 50},
                "Vegetable Biryani with Raita": {"Total Prepared": 70, "Consumed": 60},
                "Aloo Gobi with Roti": {"Total Prepared": 50, "Consumed": 40}
            },
            "Snacks": {
                "Chaat (Street Food)": {"Total Prepared": 35, "Consumed": 30},
                "Jalebi with Rabri": {"Total Prepared": 25, "Consumed": 20},
                "Masala Chai with Bhujia": {"Total Prepared": 15, "Consumed": 10}
            },
            "Dinner": {
                "Paneer Tikka Masala with Jeera Rice": {"Total Prepared": 50, "Consumed": 45},
                "Tandoori Fish with Naan": {"Total Prepared": 55, "Consumed": 50},
                "Dal Makhani with Steamed Rice": {"Total Prepared": 45, "Consumed": 35}
            }
        },
        "Day 4": {
            "Breakfast": {
                "Aloo Paratha with Dahi (Yogurt)": {"Total Prepared": 60, "Consumed": 55},
                "Poha (Flattened Rice) with Tea": {"Total Prepared": 35, "Consumed": 28},
                "Upma (Semolina Dish) with Coconut Chutney": {"Total Prepared": 30, "Consumed": 22}
    },
            "Lunch": {
        "Rajma (Kidney Beans) with Jeera Rice": {"Total Prepared": 70, "Consumed": 62},
        "Paneer Tikka with Naan": {"Total Prepared": 50, "Consumed": 42},
        "Mixed Vegetable Curry with Roti": {"Total Prepared": 50, "Consumed": 47}
    },
            "Snacks": {
        "Samosa with Green Chutney": {"Total Prepared": 30, "Consumed": 28},
        "Chai (Tea) with Pakoras": {"Total Prepared": 25, "Consumed": 18},
        "Bhel Puri": {"Total Prepared": 30, "Consumed": 27}
    },
            "Dinner": {
        "Chicken Biryani": {"Total Prepared": 60, "Consumed": 58},
        "Dal Tadka with Steamed Rice": {"Total Prepared": 40, "Consumed": 36},
        "Vegetable Pulao with Raita": {"Total Prepared": 55, "Consumed": 52}
    }
},
        "Day 5": {
            "Breakfast": {
        "Idli with Sambhar and Coconut Chutney": {"Total Prepared": 45, "Consumed": 42},
        "Aloo Poori with Pickle": {"Total Prepared": 35, "Consumed": 32},
        "Mango Lassi": {"Total Prepared": 30, "Consumed": 25}
    },
            "Lunch": {
        "Palak Paneer with Roti": {"Total Prepared": 55, "Consumed": 52},
        "Tandoori Chicken with Naan": {"Total Prepared": 50, "Consumed": 47},
        "Masoor Dal with Jeera Rice": {"Total Prepared": 40, "Consumed": 38}
    },
            "Snacks": {
        "Dahi Puri": {"Total Prepared": 20, "Consumed": 14},
        "Gulab Jamun": {"Total Prepared": 15, "Consumed": 14},
        "Chai (Tea) with Biscuits": {"Total Prepared": 30, "Consumed": 23}
    },
            "Dinner": {
        "Mutton Rogan Josh with Pulao": {"Total Prepared": 65, "Consumed": 61},
        "Chole (Chickpea Curry) with Bhature": {"Total Prepared": 45, "Consumed": 41},
        "Mixed Vegetable Fried Rice": {"Total Prepared": 50, "Consumed": 46}
    }
},
        "Day 6": {
            "Breakfast": {
        "Masala Dosa with Coconut Chutney": {"Total Prepared": 47, "Consumed": 45},
        "Aloo Paratha with Lassi": {"Total Prepared": 58, "Consumed": 58},
        "Medu Vada with Sambhar": {"Total Prepared": 36, "Consumed": 36}
    },
            "Lunch": {
        "Butter Chicken with Naan": {"Total Prepared": 54, "Consumed": 50},
        "Vegetable Biryani with Raita": {"Total Prepared": 63, "Consumed": 63},
        "Aloo Gobi with Roti": {"Total Prepared": 44, "Consumed": 44}
    },
        "Snacks": {
        "Chaat (Street Food)": {"Total Prepared": 32, "Consumed": 32},
        "Jalebi with Rabri": {"Total Prepared": 21, "Consumed": 21},
        "Masala Chai with Bhujia": {"Total Prepared": 12, "Consumed": 12}
    },
    "Dinner": {
        "Paneer Tikka Masala with Jeera Rice": {"Total Prepared": 48, "Consumed": 48},
        "Tandoori Fish with Naan": {"Total Prepared": 52, "Consumed": 52},
        "Dal Makhani with Steamed Rice": {"Total Prepared": 37, "Consumed": 37}
    }
},
        "Day 7": {
            "Breakfast": {
        "Aloo Paratha with Dahi (Yogurt)": {"Total Prepared": 55, "Consumed": 53},
        "Poha (Flattened Rice) with Tea": {"Total Prepared": 32, "Consumed": 29},
        "Upma (Semolina Dish) with Coconut Chutney": {"Total Prepared": 24, "Consumed": 21}
    },
            "Lunch": {
        "Rajma (Kidney Beans) with Jeera Rice": {"Total Prepared": 60, "Consumed": 60},
        "Paneer Tikka with Naan": {"Total Prepared": 40, "Consumed": 40},
        "Mixed Vegetable Curry with Roti": {"Total Prepared": 45, "Consumed": 45}
    },
            "Snacks": {
        "Samosa with Green Chutney": {"Total Prepared": 15, "Consumed": 15},
        "Chai (Tea) with Pakoras": {"Total Prepared": 20, "Consumed": 16},
        "Bhel Puri": {"Total Prepared": 29, "Consumed": 24}
    },
            "Dinner": {
        "Chicken Biryani": {"Total Prepared": 57, "Consumed": 57},
        "Dal Tadka with Steamed Rice": {"Total Prepared": 34, "Consumed": 34},
        "Vegetable Pulao with Raita": {"Total Prepared": 49, "Consumed": 49}
    }
}
    }
    return menu

def calculate_wastage(leftover_data, menu):
    daily_wastage = {}
    weekly_wastage = {meal: 0 for meal in ["Breakfast", "Lunch", "Snacks", "Dinner"]}
    item_wastage = {}

    for day, meals in leftover_data.items():
        daily_wastage[day] = sum(sum(meal.values()) for meal in meals.values())
        for meal_type, meal in meals.items():
            for item, quantity in meal.items():
                weekly_wastage[meal_type] += quantity
                item_wastage[item] = item_wastage.get(item, 0) + quantity

    most_wasted_item = max(weekly_wastage, key=weekly_wastage.get)

    return daily_wastage, weekly_wastage, item_wastage, most_wasted_item

def calculate_wastage_statistics(daily_wastage):
    daily_wastage_values = list(daily_wastage.values())
    mean_wastage = sum(daily_wastage_values) / len(daily_wastage_values)
    median_wastage = sorted(daily_wastage_values)[len(daily_wastage_values) // 2]
    std_deviation = statistics.stdev(daily_wastage_values)
    return mean_wastage, median_wastage, std_deviation



def collect_leftover_data(menu):
    leftover_data = {}
    for day, day_menu in menu.items():
        day_data = {}
        print(f"{day}:")
        for meal, meal_items in day_menu.items():
            meal_data = {}
            print(f"{meal}:")
            for item_name, item_quantity in meal_items.items():
                quantity = random.randint(0, 10000)
                meal_data[item_name] = quantity
            day_data[meal] = meal_data
        leftover_data[day] = day_data
    return leftover_data

def collect_leftover_data_without_wastage(menu):
    leftover_data = {}
    for day, day_menu in menu.items():
        day_data = {}
        print(f"{day}:")
        for meal, meal_items in day_menu.items():
            meal_data = {}
            print(f"{meal}:")
            for item_name, item_quantity in meal_items.items():
                quantity = 0
                meal_data[item_name] = quantity
            day_data[meal] = meal_data
        leftover_data[day] = day_data
    return leftover_data
def calculate_total_wastage(menu):
    total_prepared = {}
    total_consumed = {}

    for day in menu.values():
        for meals in day.values():
            for item, data in meals.items():
                total_prepared[item] = total_prepared.get(item, 0) + data["Total Prepared"]
                total_consumed[item] = total_consumed.get(item, 0) + data["Consumed"]

    return total_prepared, total_consumed

def calculate_percentage_wastage(total_prepared, total_consumed):
    percentage_wastage = {}
    for item, prepared in total_prepared.items():
        consumed = total_consumed.get(item, 0)
        wastage = prepared - consumed
        percentage = (wastage / prepared) * 100
        percentage_wastage[item] = percentage

    return percentage_wastage


def daily_menu_recommendations(item_wastage, menu):
    daily_recommendations = {}

    for day, meals in menu.items():
        recommendations = {"Add": [], "Remove": []}

        total_wastage = sum(item_wastage[item] for item in item_wastage if item in meals['Breakfast'] or item in meals['Lunch'] or item in meals['Snacks'] or item in meals['Dinner'])
        threshold = 0.1 * total_wastage  # 10% threshold

        add_items = []
        remove_items = []

        for item, quantity in item_wastage.items():
            if item in meals['Breakfast'] or item in meals['Lunch'] or item in meals['Snacks'] or item in meals['Dinner']:
                if quantity > threshold:
                    add_items.append(item)
                elif quantity < threshold:
                    remove_items.append(item)

        random.shuffle(add_items)
        random.shuffle(remove_items)

        for meal_category in ["Breakfast", "Lunch", "Snacks", "Dinner"]:
            if add_items:
                recommendations["Add"].append(f"{add_items.pop(0)} ({meal_category})")
            if remove_items:
                recommendations["Remove"].append(f"{remove_items.pop(0)} ({meal_category})")

        daily_recommendations[day] = recommendations

    return daily_recommendations

def create_recommendations_table(daily_recommendations):
    recommendation_tables = {}
    for day, recommendations in daily_recommendations.items():
        recommendation_table = PrettyTable()
        recommendation_table.field_names = ["Action", "Items"]
        
        for action, items in recommendations.items():
            if items:
                recommendation_table.add_row([action, ", ".join(items)])
        
        recommendation_tables[day] = recommendation_table
    return recommendation_tables

def display_recommendations_tables(daily_recommendations):
    for day, recommendations in daily_recommendations.items():
        print(f"\n{day} Recommendations:")
        print("\n")
        if recommendations:
            for action, items in recommendations.items():
                if items:
                    if action == "Add":
                        print("**ADD TO THE MENU :**")
                        print("\n")
                    elif action == "Remove":
                        print("\n")
                        print("**REMOVE FROM THE MENU :**")
                        print("\n")
                    for item in items:
                        print(f"- {item}")
        else:
            print("NO RECOMENDATIONS FOR THE DAY.")

def item_probability_of_wastage(item_wastage, threshold=50):
    probabilities = {}
    total_items = sum(item_wastage.values())

    for item, quantity in item_wastage.items():
        probability = quantity / total_items
        probabilities[item] = probability
    custom_colors = ['skyblue', 'lightgreen', 'pink', 'orange']

    items = list(probabilities.keys())
    probabilities = list(probabilities.values())

    plt.figure(figsize=(10, 6))
    plt.barh(items, probabilities, color=custom_colors, edgecolor='black', alpha=0.6) 
    plt.title("Item-based Probability of Wastage", fontsize=16, fontname='Arial')  
    plt.xlabel("Probability", fontsize=14, fontname='Calibri')  
    plt.ylabel("Menu Item", fontsize=14, fontname='Times New Roman')  
    plt.xticks(fontsize=10, fontname='Courier New')  
    plt.yticks(fontsize=8, fontname='Verdana')  
    plt.grid(axis='x', linestyle='--', alpha=0.6)
    plt.tight_layout()
    plt.show()

def create_bar_chart(daily_wastage):
    days = list(daily_wastage.keys())
    wastage = list(daily_wastage.values())

    custom_colors = ['skyblue', 'lightgreen', 'pink', 'orange']

    plt.figure(figsize=(10, 6))
    plt.bar(days, wastage, color=custom_colors, edgecolor='black', linewidth=1.2, width=0.6) 
    plt.title("Daily Food Wastage", fontsize=16, fontweight='bold') 
    plt.xlabel("Days", fontsize=12, fontweight='bold') 
    plt.ylabel("Wastage (grams)", fontsize=12, fontweight='bold') 
    plt.xticks(rotation=45, fontsize=10, fontweight='bold')  
    plt.yticks(fontsize=10, fontweight='bold') 
    plt.grid(axis='y', linestyle='--', alpha=0.6) 
    plt.tight_layout()


    for i, v in enumerate(wastage):
        plt.text(i, v, str(v), ha='center', va='bottom', fontweight='bold', fontsize=10)

    plt.show()

def top_n_items(data, n, reverse=False):

    return dict(sorted(data.items(), key=lambda item: item[1], reverse=reverse)[:n])

def create_top_items_chart(data, title, xlabel, ylabel):
    items = list(data.keys())
    values = list(data.values())

    sns.set(style="whitegrid") 

    plt.figure(figsize=(10, 6))
    ax = sns.barplot(x=items, y=values, palette="coolwarm")

    plt.title(title, fontsize=16, fontweight='bold')
    plt.xlabel(xlabel, fontsize=12, fontweight='bold')
    plt.ylabel(ylabel, fontsize=12, fontweight='bold')
    plt.xticks(rotation=45, fontsize=10, fontweight='bold')
    plt.yticks(fontsize=10, fontweight='bold')
    for i, v in enumerate(values):
        ax.text(i, v, str(v), ha='center', va='bottom', fontweight='bold', fontsize=10)

    plt.tight_layout()
    plt.show()

    
def main():
    print("College Mess Food Wastage Calculator")
    menu = create_sample_menu()
    leftover_data = collect_leftover_data(menu)
    daily_wastage, weekly_wastage, item_wastage, most_wasted_item = calculate_wastage(leftover_data, menu)
    print("\nDaily Wastage:")
    daily_wastage_table = PrettyTable()
    daily_wastage_table.field_names = ["Day", "Wastage (grams)"]
    for day, wastage in daily_wastage.items():
        daily_wastage_table.add_row([day, wastage])
    print(daily_wastage_table)
    
    create_bar_chart(daily_wastage)

    print("\nWeekly Wastage:")
    weekly_wastage_table = PrettyTable()
    weekly_wastage_table.field_names = ["Meal Type", "Wastage (grams)"]
    for meal_type, wastage in weekly_wastage.items():
        weekly_wastage_table.add_row([meal_type, wastage])
    print(weekly_wastage_table)

    most_wasted_item_name = most_wasted_item
    print(f"\nMost Wasted Item: {most_wasted_item_name} ({weekly_wastage[most_wasted_item]} grams)")

    sorted_item_wastage = dict(sorted(item_wastage.items(), key=lambda item: item[1], reverse=True))
    print("\nItem-wise Wastage (Sorted in Descending Order):")
    item_wastage_table = PrettyTable()
    item_wastage_table.field_names = ["Item", "Wastage (grams)"]
    for item, wastage in sorted_item_wastage.items():
        item_wastage_table.add_row([item, wastage])
    print(item_wastage_table)
    mean_wastage, median_wastage, std_deviation = calculate_wastage_statistics(daily_wastage)

    print("\nDaily Wastage Statistics:")
    print(f"MEAN Wastage: {mean_wastage} grams")
    print(f"MEDIAN Wastage: {median_wastage} grams")
    print(f"STANDARD DEVIATION: {std_deviation} grams")


    daily_recommendations = daily_menu_recommendations(item_wastage, menu)
    display_recommendations_tables(daily_recommendations)
    

    top_consumed_items = top_n_items(item_wastage, 5)
    top_wasted_items = top_n_items(item_wastage, 5, reverse=True)

    create_top_items_chart(top_consumed_items, "Top 5 Consumed Food Items", "Item", "Quantity (grams)")
    create_top_items_chart(top_wasted_items, "Top 5 Wasted Food Items", "Item", "Quantity (grams)")
    item_probabilities = item_probability_of_wastage(item_wastage) 

    menu = create_sample_menu()
    total_prepared, total_consumed = calculate_total_wastage(menu)
    percentage_wastage = calculate_percentage_wastage(total_prepared, total_consumed)

    table = PrettyTable()
    table.field_names = ["Item", "Total Prepared", "Total Consumed", "Percentage Wastage"]
    for item, prepared in total_prepared.items():
        consumed = total_consumed.get(item, 0)
        wastage = prepared - consumed
        table.add_row([item, prepared, consumed, f"{percentage_wastage[item]:.2f}%"])

    print(table)

    items = list(percentage_wastage.keys())
    wastage_percentages = list(percentage_wastage.values())

    colors = ['skyblue' if w <= 20 else 'lightcoral' for w in wastage_percentages]

    plt.figure(figsize=(10, 6))
    plt.barh(items, wastage_percentages, color=colors)
    plt.xlabel('Percentage Wastage')
    plt.title('Percentage Wastage of Food Items')
    plt.gca().invert_yaxis()

    for i, v in enumerate(wastage_percentages):
        plt.text(v + 1, i, f'{v:.2f}%', color='black', va='center', fontsize=10, fontweight='bold')

    plt.grid(axis='x', linestyle='--', alpha=0.6)
    plt.tight_layout()
    
    plt.show()

if __name__ == "__main__":
   main()