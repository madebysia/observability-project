import httpx
import structlog
import re
from collections import Counter

log = structlog.get_logger()

# 1. Ingesting Industry Data (LogHub HDFS Sample)
HDFS_SAMPLE_URL = "https://raw.githubusercontent.com/logpai/loghub/master/HDFS/HDFS_2k.log"

def fetch_industry_data():
    response = httpx.get(HDFS_SAMPLE_URL)
    return response.text.splitlines()

def analyze_patterns():
    raw_logs = fetch_industry_data()
    patterns = []
    
    # Simple regex to mask IP addresses and IDs for privacy (Industry best practice)
    for line in raw_logs:
        # Extract the "message" part of the HDFS log
        msg = line.split(":")[-1].strip()
        # Anonymize/Generalize (Masking digits)
        generic_pattern = re.sub(r'\d+', '<ID>', msg)
        patterns.append(generic_pattern)
    
    # 3. Root Cause Analysis (RCA) via Frequency
    counts = Counter(patterns)
    
    log.info("analysis_complete", total_logs=len(raw_logs), unique_patterns=len(counts))
    
    # Show top patterns
    for pattern, count in counts.most_common(3):
        log.info("log_pattern_found", occurrences=count, pattern=pattern)

if __name__ == "__main__":
    analyze_patterns()