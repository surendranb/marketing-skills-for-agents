import os

# Channels and Parts for grid generation
channels = [
    "LinkedIn", "Twitter", "Cold Email", "Newsletter", 
    "Landing Page", "Blog Post", "Case Study", "Whitepaper", 
    "Video Script", "Podcast Outline", "Google Ads", "Meta Ads"
]

parts = [
    "Headline", "Hook", "Intro", "Body Copy", 
    "Call to Action", "Summary", "Outline", "Conclusion"
]

# Specific skills for other domains
strategy_skills = [
    "ICP Definition", "Buyer Persona Interviewing", "Pain Point Mapping", 
    "JTBD Analysis", "SWOT Analysis", "Competitor Feature Matrix", 
    "Positioning Gap Analysis", "Value Proposition Design"
]

seo_skills = [
    "Keyword Research", "On-Page Optimization", "Meta Tag Writing", 
    "Internal Linking Strategy", "Semantic Keyword Insertion", 
    "Sitemap Generation", "Robots.txt Configuration", "Backlink Audit"
]

analytics_skills = [
    "GA4 Setup", "Conversion Tracking", "Event Tagging", 
    "UTM Parameter Design", "Attribution Modeling", "Dashboard Creation"
]

framework_skills = [
    "April Dunford Positioning", "StoryBrand SB7 Framework", "Crossing the Chasm Strategy", 
    "Permission Marketing Design", "Blue Ocean Strategy Canvas", "Hook Model Design"
]

math_skills = [
    "CAC Modeling", "LTV Prediction", "Payback Period Calculation", 
    "Funnel Velocity Audit", "Cohort Retention Analysis"
]

ops_skills = [
    "Lead Scoring Setup", "Data Enrichment Configuration", "Multi Touch Attribution", 
    "CRM Workflow Automation", "Lead Routing Logic"
]

TEMPLATE = """---
name: {slug}
version: "1.0.0"
category: {category}
difficulty: intermediate
description: {desc}
triggers:
{triggers_str}
prerequisites: []
related_skills: []
success_metrics:
{metrics_str}
---

# {name}

{desc}

## When to Use This Skill
Apply this skill when:
- Working on tasks related to {category}
- You need to execute {name_lower}

## Best Practices
1. Keep it concise and actionable.
2. Focus on B2B context.
3. Iterate based on data.

## Anti-Patterns to Avoid
- Being too generic.
- Ignoring the target audience.
"""

def generate():
    count = 0
    
    # 1. Generate Grid Skills (Copywriting & Content)
    for channel in channels:
        for part in parts:
            slug = f"{channel.lower().replace(' ', '-')}-{part.lower().replace(' ', '-')}"
            name = f"{channel} {part} Creation"
            desc = f"Create the {part.lower()} for a {channel} campaign to drive engagement."
            category = "Content Creation"
            
            triggers = [channel.lower(), part.lower(), "copywriting", "content"]
            metrics = ["click_through_rate", "engagement_rate"]
            
            folder_path = os.path.join("content_creation", channel.lower().replace(" ", "_"), slug)
            os.makedirs(folder_path, exist_ok=True)
            
            file_path = os.path.join(folder_path, "skill.md")
            content = TEMPLATE.format(
                slug=slug,
                name=name,
                desc=desc,
                category=category,
                name_lower=name.lower(),
                category_lower=category.lower(),
                triggers_str="".join([f"  - {t}\n" for t in triggers]).rstrip(),
                metrics_str="".join([f"  - {m}\n" for m in metrics]).rstrip()
            )
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(content)
            count += 1

    # 2. Generate Strategy Skills
    for skill in strategy_skills:
        slug = skill.lower().replace(' ', '-')
        name = skill
        desc = f"Execute {skill.lower()} to align business strategy and understand buyers."
        category = "Strategy & Research"
        
        triggers = ["strategy", "research", "persona", slug]
        metrics = ["strategy_alignment", "persona_accuracy"]
        
        folder_path = os.path.join("strategy_research", slug)
        os.makedirs(folder_path, exist_ok=True)
        
        file_path = os.path.join(folder_path, "skill.md")
        content = TEMPLATE.format(
            slug=slug,
            name=name,
            desc=desc,
            category=category,
            name_lower=name.lower(),
            category_lower=category.lower(),
            triggers_str="".join([f"  - {t}\n" for t in triggers]).rstrip(),
            metrics_str="".join([f"  - {m}\n" for m in metrics]).rstrip()
        )
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        count += 1

    # 3. Generate SEO Skills
    for skill in seo_skills:
        slug = skill.lower().replace(' ', '-')
        name = skill
        desc = f"Perform {skill.lower()} to improve search engine visibility and traffic."
        category = "SEO"
        
        triggers = ["seo", "keyword", "ranking", slug]
        metrics = ["organic_traffic", "keyword_ranking"]
        
        folder_path = os.path.join("seo", slug)
        os.makedirs(folder_path, exist_ok=True)
        
        file_path = os.path.join(folder_path, "skill.md")
        content = TEMPLATE.format(
            slug=slug,
            name=name,
            desc=desc,
            category=category,
            name_lower=name.lower(),
            category_lower=category.lower(),
            triggers_str="".join([f"  - {t}\n" for t in triggers]).rstrip(),
            metrics_str="".join([f"  - {m}\n" for m in metrics]).rstrip()
        )
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        count += 1

    # 4. Generate Analytics Skills
    for skill in analytics_skills:
        slug = skill.lower().replace(' ', '-')
        name = skill
        desc = f"Configure {skill.lower()} to ensure accurate data tracking and attribution."
        category = "Analytics"
        
        triggers = ["analytics", "tracking", "ga4", slug]
        metrics = ["data_accuracy", "tracking_coverage"]
        
        folder_path = os.path.join("analytics", slug)
        os.makedirs(folder_path, exist_ok=True)
        
        file_path = os.path.join(folder_path, "skill.md")
        content = TEMPLATE.format(
            slug=slug,
            name=name,
            desc=desc,
            category=category,
            name_lower=name.lower(),
            category_lower=category.lower(),
            triggers_str="".join([f"  - {t}\n" for t in triggers]).rstrip(),
            metrics_str="".join([f"  - {m}\n" for m in metrics]).rstrip()
        )
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        count += 1

    # 5. Generate Framework Skills
    for skill in framework_skills:
        slug = skill.lower().replace(' ', '-')
        name = skill
        desc = f"Apply the {skill} framework to structure marketing strategy."
        category = "Frameworks"
        
        triggers = ["framework", "strategy", slug]
        metrics = ["framework_adoption", "strategic_clarity"]
        
        folder_path = os.path.join("frameworks", slug)
        os.makedirs(folder_path, exist_ok=True)
        
        file_path = os.path.join(folder_path, "skill.md")
        content = TEMPLATE.format(
            slug=slug,
            name=name,
            desc=desc,
            category=category,
            name_lower=name.lower(),
            category_lower=category.lower(),
            triggers_str="".join([f"  - {t}\n" for t in triggers]).rstrip(),
            metrics_str="".join([f"  - {m}\n" for m in metrics]).rstrip()
        )
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        count += 1

    # 6. Generate Math Skills
    for skill in math_skills:
        slug = skill.lower().replace(' ', '-')
        name = skill
        desc = f"Execute {skill.lower()} to understand unit economics and ROI."
        category = "Marketing Math"
        
        triggers = ["math", "metrics", "finance", slug]
        metrics = ["model_accuracy", "roi"]
        
        folder_path = os.path.join("marketing_math", slug)
        os.makedirs(folder_path, exist_ok=True)
        
        file_path = os.path.join(folder_path, "skill.md")
        content = TEMPLATE.format(
            slug=slug,
            name=name,
            desc=desc,
            category=category,
            name_lower=name.lower(),
            category_lower=category.lower(),
            triggers_str="".join([f"  - {t}\n" for t in triggers]).rstrip(),
            metrics_str="".join([f"  - {m}\n" for m in metrics]).rstrip()
        )
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        count += 1

    # 7. Generate Ops Skills
    for skill in ops_skills:
        slug = skill.lower().replace(' ', '-')
        name = skill
        desc = f"Configure {skill.lower()} to optimize marketing operations and workflows."
        category = "Operations"
        
        triggers = ["operations", "workflow", "crm", slug]
        metrics = ["workflow_efficiency", "lead_quality"]
        
        folder_path = os.path.join("operations", slug)
        os.makedirs(folder_path, exist_ok=True)
        
        file_path = os.path.join(folder_path, "skill.md")
        content = TEMPLATE.format(
            slug=slug,
            name=name,
            desc=desc,
            category=category,
            name_lower=name.lower(),
            category_lower=category.lower(),
            triggers_str="".join([f"  - {t}\n" for t in triggers]).rstrip(),
            metrics_str="".join([f"  - {m}\n" for m in metrics]).rstrip()
        )
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        count += 1

    print(f"\\n✨ Successfully generated {count} skills!")

if __name__ == "__main__":
    generate()
