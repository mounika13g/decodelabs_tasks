job_roles = {
    "Data Scientist": ["python", "sql", "machine learning", "statistics"],
    "DevOps Engineer": ["aws", "docker", "kubernetes", "automation"],
    "Backend Developer": ["java", "python", "sql", "apis"],
    "Frontend Developer": ["javascript", "html", "css", "react"],
    "Cloud Architect": ["aws", "cloud computing", "automation", "kubernetes"],
}

user_skills = ["python", "cloud computing", "automation"]

scores = {}
for role, skills in job_roles.items():
    match_count = len(set(user_skills) & set(skills)) 
    scores[role] = match_count

ranked = sorted(scores.items(), key=lambda x: x[1], reverse=True)

print("Top 3 Recommended Career Paths:")
for role, count in ranked[:3]:
    print(f"{role}  ->  {count} matching skills")