import argparse
import csv
from csv_reader import read_subject_csv
# from llm_api import call_anthropic  # Uncomment if using Anthropic in your solution

# Comprehensive concept keyword dictionary for all subjects
concept_keywords = {
    # ============ ANCIENT HISTORY ============
    # Prehistoric & Harappan
    "harappan": "Harappan Civilization",
    "indus valley": "Indus Valley Civilization",
    "indus": "Indus Valley Civilization",
    "burzahom": "Neolithic Culture",
    "ganeshwar": "Chalcolithic Culture",
    "chanhudaro": "Harappan Sites",
    "kot diji": "Harappan Sites",
    "dholavira": "Harappan Water Management",
    "kalibangan": "Harappan Sites",
    "rakhigarhi": "Harappan Sites",
    "ropar": "Harappan Sites",
    "sohgaura": "Post-Harappan",
    "desalpur": "Harappan Sites",
    "terracotta": "Ancient Art",
    "copper artefacts": "Ancient Metallurgy",
    "water harvesting": "Ancient Engineering",
    
    # Vedic Period
    "vedic": "Vedic Civilization",
    "rigvedic": "Vedic Civilization",
    "aryans": "Vedic Civilization",
    "rigveda": "Vedic Literature",
    "yajnas": "Vedic Religion",
    "nature worship": "Vedic Religion",
    
    # Mauryan Empire
    "mauryan": "Mauryan Empire",
    "ashoka": "Mauryan Empire",
    "kautilya": "Kautilya's Arthashastra",
    "arthashastra": "Kautilya's Arthashastra",
    "chandragupta": "Mauryan Empire",
    "edicts": "Ashokan Edicts",
    "kanganahalli": "Ashokan Monuments",
    "sanchi": "Buddhist Architecture",
    "shahbazgarhi": "Ashokan Edicts",
    "james prinsep": "Epigraphy",
    
    # Gupta Period
    "gupta": "Gupta Empire",
    "guptas": "Gupta Empire",
    "samudragupta": "Gupta Empire",
    "chandra gupta": "Gupta Empire",
    "kalidasa": "Gupta Literature",
    "vishti": "Gupta Administration",
    "ghantasala": "Gupta Trade",
    "kadura": "Gupta Trade",
    "chaul": "Gupta Trade",
    "forced labour": "Ancient Labor Systems",
    
    # Post-Gupta
    "harshavardhana": "Post-Gupta Period",
    "harsha": "Post-Gupta Period",
    "pushyabhutis": "Post-Gupta Kingdoms",
    "maukharis": "Post-Gupta Kingdoms",
    "maitrakas": "Post-Gupta Kingdoms",
    "paramaras": "Post-Gupta Kingdoms",
    "yadavas": "Post-Gupta Kingdoms",
    
    # Religion & Philosophy
    "buddhism": "Buddhism",
    "buddhist": "Buddhism",
    "jainism": "Jainism",
    "jain": "Jainism",
    "dignaga": "Buddhist Philosophy",
    "aryadeva": "Buddhist Philosophy",
    "nathamuni": "Vaishnavism",
    "nettipakarana": "Buddhist Texts",
    "parishishta parvan": "Jaina Literature",
    "avadanasataka": "Buddhist Literature",
    "trishashtilakshana": "Jaina Literature",
    
    # Literature & Scholars
    "panini": "Ancient Grammar",
    "amarasimha": "Sanskrit Literature",
    "bhavabhuti": "Sanskrit Drama",
    "hastimalla": "Sanskrit Drama",
    "kshemeshvara": "Sanskrit Drama",
    "playwrights": "Sanskrit Drama",
    
    # Administration & Society
    "eripatti": "Medieval Land Revenue",
    "taniyurs": "Medieval Administration",
    "ghatikas": "Ancient Education",
    "shrenis": "Ancient Guilds",
    "guilds": "Ancient Guilds",
    "kulyavapa": "Ancient Measurements",
    "dronavapa": "Ancient Measurements",
    "measurement of land": "Ancient Measurements",
    "magadha": "Ancient Professions",
    
    # Science & Technology
    "surgical instruments": "Ancient Medicine",
    "sine": "Ancient Mathematics",
    "cyclic quadrilateral": "Ancient Mathematics",
    "scientific progress": "Ancient Science",
    
    # Trade & Travel
    "yuan chwang": "Chinese Travelers",
    "hiuen tsang": "Chinese Travelers",
    "maritime": "Ancient Trade",
    "bay of bengal": "Ancient Maritime Trade",
    "southeast asia": "Ancient Trade",
    "ports": "Ancient Trade",
    "foreign trade": "Ancient Trade",
    
    # ============ MATHEMATICS ============
    "profit": "Profit and Loss",
    "loss": "Profit and Loss",
    "percentage": "Percentages",
    "percent": "Percentages",
    "discount": "Discount and Markup",
    "markup": "Discount and Markup",
    "compound interest": "Compound Interest",
    "simple interest": "Simple Interest",
    "ratio": "Ratios and Proportions",
    "proportion": "Ratios and Proportions",
    "alloy": "Mixtures and Alloys",
    "mixture": "Mixtures and Alloys",
    "investment": "Partnership and Investment",
    "share": "Partnership and Investment",
    "partnership": "Partnership and Investment",
    "probability": "Probability",
    "outcomes": "Probability",
    "die": "Probability",
    "dice": "Probability",
    "throws": "Probability",
    "combinations": "Combinatorics",
    "permutations": "Combinatorics",
    "ordered triplets": "Combinatorics",
    "arithmetic progression": "Sequences and Series",
    "geometric progression": "Sequences and Series",
    "sequence": "Sequences and Series",
    "series": "Sequences and Series",
    "goods": "Commercial Mathematics",
    "merchant": "Commercial Mathematics",
    "trader": "Commercial Mathematics",
    "cost price": "Cost Price and Selling Price",
    "selling price": "Cost Price and Selling Price",
    "efficiency": "Work and Time",
    "workers": "Work and Time",
    "work": "Work and Time",
    "rate": "Rate and Speed",
    "speed": "Rate and Speed",
    
    # ============ PHYSICS ============
    "force": "Force and Motion",
    "newton": "Force and Motion",
    "motion": "Kinematics",
    "velocity": "Kinematics",
    "acceleration": "Kinematics",
    "newton's law": "Newton's Laws",
    "newton's first law": "Newton's Laws",
    "newton's second law": "Newton's Laws",
    "newton's third law": "Newton's Laws",
    "rest": "Newton's Laws",
    "external force": "Newton's Laws",
    "circular motion": "Circular Motion",
    "si unit": "Units and Measurements",
    "joule": "Energy and Work",
    "watt": "Power",
    "pascal": "Pressure",
    "energy": "Energy and Work",
    "work": "Energy and Work",
    "power": "Power",
    "pressure": "Pressure",
    "momentum": "Momentum",
    "friction": "Friction",
    "gravity": "Gravitation",
    "gravitational": "Gravitation",
    "mass": "Mass and Weight",
    "weight": "Mass and Weight",
    "displacement": "Kinematics",
    "distance": "Kinematics",
    "time": "Time and Motion",
    
    # ============ ECONOMICS ============
    "gdp": "Gross Domestic Product",
    "gross domestic product": "Gross Domestic Product",
    "inflation": "Inflation",
    "consumer price index": "Price Indices",
    "cpi": "Price Indices",
    "gnp": "Gross National Product",
    "gross national product": "Gross National Product",
    "per capita income": "National Income",
    "exchange rate": "Foreign Exchange",
    "supply": "Supply and Demand",
    "demand": "Supply and Demand",
    "market": "Market Economics",
    "monopoly": "Market Structure",
    "competition": "Market Structure",
    "fiscal policy": "Government Policy",
    "monetary policy": "Government Policy",
    "taxation": "Public Finance",
    "budget": "Public Finance",
    "unemployment": "Labor Economics",
    "employment": "Labor Economics",
    "recession": "Economic Cycles",
    "depression": "Economic Cycles",
    "economic growth": "Economic Development",
    "development": "Economic Development",
    "trade": "International Trade",
    "import": "International Trade",
    "export": "International Trade",
    "balance of payments": "International Economics",
    "currency": "Money and Banking",
    "banking": "Money and Banking",
    "interest rate": "Money and Banking",
    "microeconomics": "Microeconomics",
    "macroeconomics": "Macroeconomics",
}

def extract_concepts_keyword_based(question):
    """Extract concepts using keyword mapping only"""
    question_lower = question.lower()
    concepts = set()
    
    # Check for exact keyword matches
    for keyword, concept in concept_keywords.items():
        if keyword in question_lower:
            concepts.add(concept)
    
    # Subject-specific pattern matching
    # Ancient History patterns
    if any(term in question_lower for term in ["ancient india", "indian history"]):
        concepts.add("Ancient Indian History")
    if "cultural history" in question_lower:
        concepts.add("Ancient Culture")
    if "historical person" in question_lower:
        concepts.add("Ancient Personalities")
    if "jaina texts" in question_lower:
        concepts.add("Jaina Literature")
    if "buddhist scholar" in question_lower:
        concepts.add("Buddhism")
    if "vaishnava scholar" in question_lower:
        concepts.add("Vaishnavism")
    
    # Mathematics patterns
    if any(term in question_lower for term in ["rs.", "rupees", "₹"]):
        concepts.add("Commercial Mathematics")
    if "%" in question_lower or "percent" in question_lower:
        concepts.add("Percentages")
    if any(term in question_lower for term in ["minimum", "maximum", "range"]):
        concepts.add("Optimization")
    if "overall" in question_lower and "profit" in question_lower:
        concepts.add("Profit and Loss")
    
    # Physics patterns
    if "si unit" in question_lower:
        concepts.add("Units and Measurements")
    if "according to" in question_lower and "law" in question_lower:
        concepts.add("Physical Laws")
    
    # Economics patterns
    if "stands for" in question_lower:
        concepts.add("Economic Terminology")
    if "measured by" in question_lower:
        concepts.add("Economic Indicators")
    
    return "; ".join(sorted(concepts)) if concepts else None

def extract_concepts_llm_based(question, subject):
    """Extract concepts using LLM only"""
    # Create a subject-specific prompt for better LLM performance
    subject_context = {
        'ancient_history': 'ancient Indian history, civilizations, empires, religion, culture, and historical personalities',
        'math': 'mathematics including algebra, geometry, probability, statistics, and commercial mathematics',
        'physics': 'physics including mechanics, thermodynamics, waves, electricity, and scientific laws',
        'economics': 'economics including microeconomics, macroeconomics, economic indicators, and policy'
    }
    
    context = subject_context.get(subject, 'academic concepts')
    prompt = f"""You are an expert in {context}. Analyze this question and identify the main academic concepts being tested.

Question: {question}

Instructions:
1. Identify 2-4 specific academic concepts that this question tests
2. Use standard academic terminology
3. Focus on the core knowledge areas being examined
4. Provide concepts in order of importance

Return only the concepts, separated by semicolons (;)."""
    
    # concept_result = call_anthropic(prompt)  # Uncomment to use LLM
    concept_result = f"LLM Generated Concept for {subject.title()}"  # Placeholder when LLM is not available
    
    return concept_result if concept_result else "Unknown"

def main():
    parser = argparse.ArgumentParser(description="Intern Test Task: Question to Concept Mapping")
    parser.add_argument('--subject', required=True, choices=['ancient_history', 'math', 'physics', 'economics'], help='Subject to process')
    parser.add_argument('--method', choices=['keyword', 'llm', 'hybrid'], default='hybrid', help='Method to use for concept extraction')
    args = parser.parse_args()

    data = read_subject_csv(args.subject)
    print(f"Loaded {len(data)} questions for subject: {args.subject}")
    print(f"Using method: {args.method}")

    # --- PLACEHOLDER FOR USER CODE ---
    # TODO: Implement your question-to-concept mapping logic here.
    # For example, iterate over data and map questions to concepts.
    # You can use the call_anthropic function from llm_api.py if needed.
    # Example:
    
    output_rows = []
    for row in data:
        question_num = row.get('Question Number', '')
        question = row['Question']
        concepts = None
        
        # Case 1: Keyword-based extraction only
        if args.method == 'keyword':
            concepts = extract_concepts_keyword_based(question)
            if not concepts:
                concepts = "Unknown"
            method_used = "Keyword"
        
        # Case 2: LLM-based extraction only
        elif args.method == 'llm':
            concepts = extract_concepts_llm_based(question, args.subject)
            method_used = "LLM"
        
        # Case 3: Hybrid approach (keyword first, then LLM)
        else:  # hybrid
            concepts = extract_concepts_keyword_based(question)
            if concepts:
                method_used = "Keyword"
            else:
                concepts = extract_concepts_llm_based(question, args.subject)
                method_used = "LLM"
        
        # Store results (without Method column)
        output_rows.append({
            "Question Number": question_num,
            "Question": question,
            "Concepts": concepts
        })
        
        print(f"Question {question_num} [{method_used}]: {concepts}")
    
    # Write results to CSV (without Method column)
    output_filename = f"output_concepts_{args.method}.csv"
    with open(output_filename, "w", newline='', encoding="utf-8") as fout:
        writer = csv.DictWriter(fout, fieldnames=["Question Number", "Question", "Concepts"])
        writer.writeheader()
        writer.writerows(output_rows)
    
    print(f"Successfully processed {len(output_rows)} questions and saved to {output_filename}")
    
    # Summary statistics
    keyword_count = sum(1 for row in output_rows if method_used == "Keyword")
    llm_count = sum(1 for row in output_rows if method_used == "LLM")
    print(f"\nSummary:")
    print(f"- Keyword-based extractions: {keyword_count}")
    print(f"- LLM-based extractions: {llm_count}")
    # ----------------------------------

if __name__ == "__main__":
    main()
