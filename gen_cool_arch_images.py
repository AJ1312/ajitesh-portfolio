import os
from PIL import Image, ImageDraw, ImageFont

def draw_sentinel_diagram():
    # 1200 x 540 crisp broadsheet diagram
    img = Image.new('RGB', (1200, 540), color='#fcfaf7')
    draw = ImageDraw.Draw(img)
    
    # Outer double border (newspaper style)
    draw.rectangle([10, 10, 1190, 530], outline='#111111', width=3)
    draw.rectangle([15, 15, 1185, 525], outline='#111111', width=1)
    
    # Title Banner
    draw.rectangle([15, 15, 1185, 65], fill='#111111')
    
    try:
        font_title = ImageFont.truetype("/System/Library/Fonts/Supplemental/Georgia.ttf", 22)
        font_box_t = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial.ttf", 16)
        font_box_s = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial.ttf", 13)
        font_arrow = ImageFont.truetype("/System/Library/Fonts/Supplemental/Georgia.ttf", 26)
    except:
        font_title = font_box_t = font_box_s = font_arrow = ImageFont.load_default()

    draw.text((30, 26), "SENTINEL-STREAM: SYSTEM ARCHITECTURE & THREAT DETECTION PIPELINE", fill='#ffffff', font=font_title)
    
    # 5 Pipeline Boxes
    stages = [
        ("1. Event Ingestion", "Raw Audit Logs & Kafka Stream"),
        ("2. O(1) EWMA Profiler", "2 KB Fixed Memory per User"),
        ("3. Stage 1: IsoForest", "Cold-Start Risk Scoring"),
        ("4. Stage 2: LightGBM", "Multi-Class Threat Classifier"),
        ("5. TreeSHAP Engine", "Sub-30µs Feature Explanation")
    ]
    
    x_positions = [40, 270, 500, 730, 960]
    box_w = 195
    box_h = 130
    y_pos = 110
    
    for idx, (t, s) in enumerate(stages):
        x = x_positions[idx]
        # Box background
        draw.rectangle([x, y_pos, x + box_w, y_pos + box_h], fill='#f5f2eb', outline='#111111', width=2)
        # Header line inside box
        draw.line([x, y_pos + 45, x + box_w, y_pos + 45], fill='#111111', width=1)
        
        draw.text((x + 10, y_pos + 15), t, fill='#111111', font=font_box_t)
        draw.text((x + 10, y_pos + 60), s, fill='#555555', font=font_box_s)
        
        # Red Arrow
        if idx < 4:
            draw.text((x + box_w + 10, y_pos + 45), "➔", fill='#d92323', font=font_arrow)
            
    # Explanatory Callout Box at Bottom
    draw.rectangle([40, 280, 1160, 500], fill='#ffffff', outline='#111111', width=2)
    draw.rectangle([40, 280, 1160, 320], fill='#111111')
    draw.text((55, 292), "HOW IT WORKS — STEP-BY-STEP EXPLANATION", fill='#ffffff', font=font_box_t)
    
    bullets = [
        "• Step 1 & 2: As millions of events stream in, the system continuously updates user habits in 2 KB of memory without saving raw logs.",
        "• Step 3 & 4: New or unknown users pass through Stage 1 (Isolation Forest), then Stage 2 (LightGBM) classifies the exact threat type.",
        "• Step 5: Instead of a mysterious score, TreeSHAP instantly hands security analysts the exact human reason for the alert in <3ms."
    ]
    
    for i, b in enumerate(bullets):
        draw.text((60, 340 + (i * 45)), b, fill='#111111', font=font_box_s)

    os.makedirs("images/architecture", exist_ok=True)
    img.save("images/architecture/sentinel_stream_arch.png")
    print("Saved images/architecture/sentinel_stream_arch.png")

def draw_cipherpulse_diagram():
    # 1200 x 540 broadsheet diagram
    img = Image.new('RGB', (1200, 540), color='#fcfaf7')
    draw = ImageDraw.Draw(img)
    
    # Outer double border
    draw.rectangle([10, 10, 1190, 530], outline='#111111', width=3)
    draw.rectangle([15, 15, 1185, 525], outline='#111111', width=1)
    
    # Title Banner
    draw.rectangle([15, 15, 1185, 65], fill='#111111')
    
    try:
        font_title = ImageFont.truetype("/System/Library/Fonts/Supplemental/Georgia.ttf", 22)
        font_box_t = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial.ttf", 16)
        font_box_s = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial.ttf", 13)
        font_arrow = ImageFont.truetype("/System/Library/Fonts/Supplemental/Georgia.ttf", 26)
    except:
        font_title = font_box_t = font_box_s = font_arrow = ImageFont.load_default()

    draw.text((30, 26), "CIPHERPULSE: LOCK-FREE ENCRYPTED TRAFFIC INSPECTION PIPELINE", fill='#ffffff', font=font_title)
    
    # 5 Pipeline Boxes
    stages = [
        ("1. RAW Capture", "AF_PACKET / eBPF Zero-Copy"),
        ("2. Consistent Router", "5-Tuple Hashing (No Mutex)"),
        ("3. Fast-Path Threads", "Lock-Free Ring Queue per Core"),
        ("4. JA4+ Fingerprint", "ClientHello TLS Signatures"),
        ("5. Beacon Classifier", "Welford Flow Rhythm Check")
    ]
    
    x_positions = [40, 270, 500, 730, 960]
    box_w = 195
    box_h = 130
    y_pos = 110
    
    for idx, (t, s) in enumerate(stages):
        x = x_positions[idx]
        draw.rectangle([x, y_pos, x + box_w, y_pos + box_h], fill='#f5f2eb', outline='#111111', width=2)
        draw.line([x, y_pos + 45, x + box_w, y_pos + 45], fill='#111111', width=1)
        
        draw.text((x + 10, y_pos + 15), t, fill='#111111', font=font_box_t)
        draw.text((x + 10, y_pos + 60), s, fill='#555555', font=font_box_s)
        
        if idx < 4:
            draw.text((x + box_w + 10, y_pos + 45), "➔", fill='#d92323', font=font_arrow)
            
    # Explanatory Callout Box at Bottom
    draw.rectangle([40, 280, 1160, 500], fill='#ffffff', outline='#111111', width=2)
    draw.rectangle([40, 280, 1160, 320], fill='#111111')
    draw.text((55, 292), "HOW IT WORKS — STEP-BY-STEP EXPLANATION", fill='#ffffff', font=font_box_t)
    
    bullets = [
        "• Step 1 & 2: Network packets arrive directly from kernel sockets and are hashed by 5-tuple so all packets of a flow hit the same CPU core.",
        "• Step 3: Every CPU core processes its own lock-free ring queue with zero mutex locking, scaling linearly across hardware threads.",
        "• Step 4 & 5: Extracts outer JA4+ handshake signatures and measures packet arrival timing to spot encrypted hacker C2 signals."
    ]
    
    for i, b in enumerate(bullets):
        draw.text((60, 340 + (i * 45)), b, fill='#111111', font=font_box_s)

    img.save("images/architecture/cipherpulse_arch.png")
    print("Saved images/architecture/cipherpulse_arch.png")

draw_sentinel_diagram()
draw_cipherpulse_diagram()
