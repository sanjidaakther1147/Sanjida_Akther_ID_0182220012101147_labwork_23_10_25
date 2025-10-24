def analyze_grades(grade_list):
    grades = [int(g) for g in grade_list]
    high_scores = [g for g in grades if g >= 80]
    low_scores = [g for g in grades if g < 80]
    a_grades = [g for g in grades if g >= 90]
    avg_high = sum(high_scores) / len(high_scores) if high_scores else 0
    low_scores_desc = sorted(low_scores, reverse=True)
    a_count = len(a_grades)
    return [avg_high, low_scores_desc, a_count]

grades = ["85", "92", "78", "88", "95", "73", "91"]
result = analyze_grades(grades)

print(f"Average of high scorers (80+): {result[0]:.1f}")
print(f"Below 80 grades: {result[1]}")
print(f"Students with A grade (90+): {result[2]}")
