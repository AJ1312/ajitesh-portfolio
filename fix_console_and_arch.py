import os
from PIL import Image, ImageDraw, ImageFont

def render_sentinel_arch(path):
    # High DPI (2400 x 1080) supersampled down to 1200 x 540 for razor-sharp text
    scale = 2
    img = Image.new('RGB', (1200 * scale, 540 * scale), color='#fcfaf7')
    draw = ImageDraw.Draw(img)
    
    # Double border
    draw.rectangle([10 * scale, 10 * scale, 1190 * scale, 530 * scale], outline='#111111', width=3 * scale)
    draw.rectangle([16 * scale, 16 * scale, 1184 * scale, 524 * scale], outline='#111111', width=1 * scale)
    
    # Header Banner
    draw.rectangle([16 * scale, 16 * scale, 1184 * scale, 70 * scale], fill='#111111')
    
    try:
        f_title = ImageFont.truetype("/System/Library/Fonts/Supplemental/Georgia.ttf", 22 * scale)
        f_box_t = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial Bold.ttf", 15 * scale)
        f_box_s = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial.ttf", 13 * scale)
        f_arrow = ImageFont.truetype("/System/Library/Fonts/Supplemental/Georgia.ttf", 28 * scale)
    except:
        f_title = f_box_t = f_box_s = f_arrow = ImageFont.load_default()

    draw.text((30 * scale, 24 * scale), "SENTINEL-STREAM: O(1) STREAMING ANOMALY DETECTION ARCHITECTURE", fill='#ffffff', font=f_title)
    
    stages = [
        ("1. Event Ingestion", "Kafka Stream / API Logs"),
        ("2. O(1) EWMA Profiler", "2 KB Fixed RAM / User"),
        ("3. Stage 1: IsoForest", "Cold-Start Risk Score"),
        ("4. Stage 2: LightGBM", "Multi-Class Classifier"),
        ("5. TreeSHAP Engine", "Per-Alert Feature Why")
    ]
    
    x_positions = [40, 270, 500, 730, 960]
    box_w = 195
    box_h = 135
    y_pos = 115
    
    for idx, (t, s) in enumerate(stages):
        x = x_positions[idx]
        draw.rectangle([x * scale, y_pos * scale, (x + box_w) * scale, (y_pos + box_h) * scale], fill='#f5f2eb', outline='#111111', width=2 * scale)
        draw.line([x * scale, (y_pos + 42) * scale, (x + box_w) * scale, (y_pos + 42) * scale], fill='#111111', width=1 * scale)
        
        draw.text(((x + 10) * scale, (y_pos + 12) * scale), t, fill='#111111', font=f_box_t)
        draw.text(((x + 10) * scale, (y_pos + 55) * scale), s, fill='#444444', font=f_box_s)
        
        if idx < 4:
            draw.text(((x + box_w + 8) * scale, (y_pos + 42) * scale), "➔", fill='#d92323', font=f_arrow)
            
    # Bottom callout box
    draw.rectangle([40 * scale, 290 * scale, 1160 * scale, 500 * scale], fill='#ffffff', outline='#111111', width=2 * scale)
    draw.rectangle([40 * scale, 290 * scale, 1160 * scale, 330 * scale], fill='#111111')
    draw.text((55 * scale, 300 * scale), "HOW THE PIPELINE WORKS — STEP-BY-STEP", fill='#ffffff', font=f_box_t)
    
    bullets = [
        "1. Ingestion & Profiler: Continuous streaming updates user activity profiles in 2 KB of fixed RAM per entity without saving raw event logs.",
        "2. Two-Stage AI Pipeline: Handles zero-history entities via Stage 1 Isolation Forest, then predicts exact attack type via Stage 2 LightGBM.",
        "3. TreeSHAP Explainability: Calculates exact Shapley value feature attributions in <30µs, giving analysts clear human reasons for every alert."
    ]
    
    for i, b in enumerate(bullets):
        draw.text((60 * scale, (350 + (i * 45)) * scale), b, fill='#111111', font=f_box_s)

    # Resize down for super crisp quality
    img_resized = img.resize((1200, 540), Image.Resampling.LANCZOS)
    img_resized.save(path)
    print(f"Saved {path}")

def render_cipherpulse_arch(path):
    scale = 2
    img = Image.new('RGB', (1200 * scale, 540 * scale), color='#fcfaf7')
    draw = ImageDraw.Draw(img)
    
    draw.rectangle([10 * scale, 10 * scale, 1190 * scale, 530 * scale], outline='#111111', width=3 * scale)
    draw.rectangle([16 * scale, 16 * scale, 1184 * scale, 524 * scale], outline='#111111', width=1 * scale)
    
    draw.rectangle([16 * scale, 16 * scale, 1184 * scale, 70 * scale], fill='#111111')
    
    try:
        f_title = ImageFont.truetype("/System/Library/Fonts/Supplemental/Georgia.ttf", 22 * scale)
        f_box_t = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial Bold.ttf", 15 * scale)
        f_box_s = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial.ttf", 13 * scale)
        f_arrow = ImageFont.truetype("/System/Library/Fonts/Supplemental/Georgia.ttf", 28 * scale)
    except:
        f_title = f_box_t = f_box_s = f_arrow = ImageFont.load_default()

    draw.text((30 * scale, 24 * scale), "CIPHERPULSE: LOCK-FREE ENCRYPTED DPI INSPECTION PIPELINE", fill='#ffffff', font=f_title)
    
    stages = [
        ("1. RAW Capture", "AF_PACKET / eBPF Socket"),
        ("2. 5-Tuple Router", "Zero-Mutex Hashing"),
        ("3. Fast-Path Threads", "Lock-Free Ring Queue"),
        ("4. JA4+ Profiler", "TLS ClientHello Signatures"),
        ("5. Beacon Classifier", "Welford Flow Timing CoV")
    ]
    
    x_positions = [40, 270, 500, 730, 960]
    box_w = 195
    box_h = 135
    y_pos = 115
    
    for idx, (t, s) in enumerate(stages):
        x = x_positions[idx]
        draw.rectangle([x * scale, y_pos * scale, (x + box_w) * scale, (y_pos + box_h) * scale], fill='#f5f2eb', outline='#111111', width=2 * scale)
        draw.line([x * scale, (y_pos + 42) * scale, (x + box_w) * scale, (y_pos + 42) * scale], fill='#111111', width=1 * scale)
        
        draw.text(((x + 10) * scale, (y_pos + 12) * scale), t, fill='#111111', font=f_box_t)
        draw.text(((x + 10) * scale, (y_pos + 55) * scale), s, fill='#444444', font=f_box_s)
        
        if idx < 4:
            draw.text(((x + box_w + 8) * scale, (y_pos + 42) * scale), "➔", fill='#d92323', font=f_arrow)
            
    draw.rectangle([40 * scale, 290 * scale, 1160 * scale, 500 * scale], fill='#ffffff', outline='#111111', width=2 * scale)
    draw.rectangle([40 * scale, 290 * scale, 1160 * scale, 330 * scale], fill='#111111')
    draw.text((55 * scale, 300 * scale), "HOW THE PIPELINE WORKS — STEP-BY-STEP", fill='#ffffff', font=f_box_t)
    
    bullets = [
        "1. Ingestion & Hash Routing: Packets are captured directly from kernel sockets and hashed by 5-tuple to pin flows to dedicated CPU cores.",
        "2. Lock-Free Execution: Every worker thread processes its isolated flow table with zero cross-thread mutex locking on the hot path.",
        "3. JA4+ & Timing ETI: Extracts outer TLS handshake signatures and measures packet inter-arrival timing to flag encrypted C2 beaconing."
    ]
    
    for i, b in enumerate(bullets):
        draw.text((60 * scale, (350 + (i * 45)) * scale), b, fill='#111111', font=f_box_s)

    img_resized = img.resize((1200, 540), Image.Resampling.LANCZOS)
    img_resized.save(path)
    print(f"Saved {path}")

os.makedirs("images/architecture", exist_ok=True)
render_sentinel_arch("images/architecture/sentinel_stream_arch.png")
render_cipherpulse_arch("images/architecture/cipherpulse_arch.png")
