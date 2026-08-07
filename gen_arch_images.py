import os
from PIL import Image, ImageDraw, ImageFont

def create_sentinel_arch_image(filepath):
    # Create a 1200x500 broadsheet styled architecture diagram PNG
    img = Image.new('RGB', (1200, 520), color='#fdfbf7')
    draw = ImageDraw.Draw(img)
    
    # Border
    draw.rectangle([10, 10, 1190, 510], outline='#111111', width=3)
    draw.rectangle([15, 15, 1185, 505], outline='#111111', width=1)
    
    # Title Banner
    draw.rectangle([15, 15, 1185, 65], fill='#111111')
    
    # Text helper
    try:
        title_font = ImageFont.truetype("/System/Library/Fonts/Supplemental/Georgia.ttf", 22)
        node_title_font = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial.ttf", 16)
        node_sub_font = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial.ttf", 13)
        arrow_font = ImageFont.truetype("/System/Library/Fonts/Supplemental/Georgia.ttf", 26)
    except:
        title_font = node_title_font = node_sub_font = arrow_font = ImageFont.load_default()

    draw.text((30, 26), "SENTINEL-STREAM: END-TO-END SYSTEM ARCHITECTURE PIPELINE", fill='#fdfbf7', font=title_font)
    
    nodes = [
        ("1. Event Stream Ingestion", "JSON Logs / Kafka Data Stream"),
        ("2. O(1) EWMA Profiler", "4 KB Fixed Matrix / User Footprint"),
        ("3. Stage 1: IsoForest", "Structural Cold-Start Risk Score"),
        ("4. Stage 2: LightGBM", "Multi-Class Threat Classifier"),
        ("5. Inline TreeSHAP", "Sub-30µs Explanation Rationale")
    ]
    
    x_starts = [40, 270, 500, 730, 960]
    box_w = 195
    box_h = 130
    y_pos = 120
    
    for i, (title, sub) in enumerate(nodes):
        x = x_starts[i]
        # Box background
        draw.rectangle([x, y_pos, x + box_w, y_pos + box_h], fill='#f5f2eb', outline='#111111', width=2)
        # Title
        draw.text((x + 12, y_pos + 20), title, fill='#111111', font=node_title_font)
        # Subtext
        draw.text((x + 12, y_pos + 65), sub, fill='#666666', font=node_sub_font)
        
        # Arrow to next node
        if i < len(nodes) - 1:
            arrow_x = x + box_w + 10
            draw.text((arrow_x, y_pos + 45), "➔", fill='#d92323', font=arrow_font)
            
    # Explanatory Callout Banner at Bottom
    draw.rectangle([40, 290, 1160, 480], fill='#ffffff', outline='#111111', width=2)
    draw.text((60, 310), "EXPLAINED PIPELINE STAGES:", fill='#d92323', font=node_title_font)
    
    explanations = [
        "• Stage 1 (Ingestion & EWMA): Continuously tracks user behavioral metrics in a fixed 2 KB memory sketch without full history.",
        "• Stage 2 (Two-Stage Inference): Handles brand-new users via Isolation Forest, then predicts exact attack type via LightGBM.",
        "• Stage 3 (TreeSHAP Explanation): Translates mathematical model weights into clear, human-readable risk factors in <30 microseconds."
    ]
    
    for idx, exp in enumerate(explanations):
        draw.text((60, 350 + (idx * 40)), exp, fill='#111111', font=node_sub_font)
        
    img.save(filepath)
    print(f"Saved {filepath}")

def create_cipherpulse_arch_image(filepath):
    # Create a 1200x520 broadsheet styled architecture diagram PNG
    img = Image.new('RGB', (1200, 520), color='#fdfbf7')
    draw = ImageDraw.Draw(img)
    
    # Border
    draw.rectangle([10, 10, 1190, 510], outline='#111111', width=3)
    draw.rectangle([15, 15, 1185, 505], outline='#111111', width=1)
    
    # Title Banner
    draw.rectangle([15, 15, 1185, 65], fill='#111111')
    
    try:
        title_font = ImageFont.truetype("/System/Library/Fonts/Supplemental/Georgia.ttf", 22)
        node_title_font = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial.ttf", 16)
        node_sub_font = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial.ttf", 13)
        arrow_font = ImageFont.truetype("/System/Library/Fonts/Supplemental/Georgia.ttf", 26)
    except:
        title_font = node_title_font = node_sub_font = arrow_font = ImageFont.load_default()

    draw.text((30, 26), "CIPHERPULSE: LOCK-FREE C++17 DPI FAST-PATH PIPELINE", fill='#fdfbf7', font=title_font)
    
    nodes = [
        ("1. RAW Capture", "AF_PACKET / eBPF Direct Socket"),
        ("2. Consistent Hash", "Zero-Mutex 5-Tuple Router"),
        ("3. Fast-Path Ring", "C++17 Lock-Free Thread Queue"),
        ("4. JA4+ Profiler", "Outer TLS Handshake Fingerprint"),
        ("5. ETI Classifier", "Non-SNI C2 Beaconing Alert")
    ]
    
    x_starts = [40, 270, 500, 730, 960]
    box_w = 195
    box_h = 130
    y_pos = 120
    
    for i, (title, sub) in enumerate(nodes):
        x = x_starts[i]
        draw.rectangle([x, y_pos, x + box_w, y_pos + box_h], fill='#f5f2eb', outline='#111111', width=2)
        draw.text((x + 12, y_pos + 20), title, fill='#111111', font=node_title_font)
        draw.text((x + 12, y_pos + 65), sub, fill='#666666', font=node_sub_font)
        
        if i < len(nodes) - 1:
            arrow_x = x + box_w + 10
            draw.text((arrow_x, y_pos + 45), "➔", fill='#d92323', font=arrow_font)
            
    # Explanatory Callout Banner at Bottom
    draw.rectangle([40, 290, 1160, 480], fill='#ffffff', outline='#111111', width=2)
    draw.text((60, 310), "EXPLAINED PIPELINE STAGES:", fill='#d92323', font=node_title_font)
    
    explanations = [
        "• Stage 1 (Zero-Copy Capture): eBPF captures raw network packets directly from the NIC kernel buffer at line-rate speed.",
        "• Stage 2 (Lock-Free Dispatch): Consistent 5-tuple hashing routes flow packets to dedicated worker CPU cores without mutex locks.",
        "• Stage 3 (Fingerprint & Rhythm ETI): Inspects outer JA4+ TLS handshakes and Welford flow periodicity to detect hacker C2 beaconing."
    ]
    
    for idx, exp in enumerate(explanations):
        draw.text((60, 350 + (idx * 40)), exp, fill='#111111', font=node_sub_font)
        
    img.save(filepath)
    print(f"Saved {filepath}")

os.makedirs("images/architecture", exist_ok=True)
create_sentinel_arch_image("images/architecture/sentinel_stream_pipeline.png")
create_cipherpulse_arch_image("images/architecture/cipherpulse_pipeline.png")
