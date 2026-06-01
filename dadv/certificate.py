from PIL import Image, ImageDraw, ImageFont
import os
from datetime import datetime

def generate_certificate(player_name, score, levels_completed):
    """
    Generates a beautiful Atmanirbhar Bharat Champion certificate
    and saves it to the user's Desktop as a PNG image.
    """
    # --- Canvas Setup ---
    WIDTH, HEIGHT = 1200, 850
    img = Image.new("RGB", (WIDTH, HEIGHT), color="#FFFDF7")
    draw = ImageDraw.Draw(img)

    # --- Indian Flag Color Scheme ---
    SAFFRON = "#FF6F00"
    GREEN = "#0A7E07"
    NAVY = "#1A237E"
    GOLD = "#FFD700"
    LIGHT_SAFFRON = "#FFF3E0"
    
    # --- Outer Decorative Borders ---
    # Saffron outer border
    draw.rectangle([0, 0, WIDTH-1, HEIGHT-1], outline=SAFFRON, width=18)
    # Green inner border
    draw.rectangle([22, 22, WIDTH-23, HEIGHT-23], outline=GREEN, width=8)
    # Navy innermost border
    draw.rectangle([38, 38, WIDTH-39, HEIGHT-39], outline=NAVY, width=3)

    # --- Saffron Top Banner ---
    draw.rectangle([0, 0, WIDTH, 120], fill=SAFFRON)
    draw.rectangle([0, 120, WIDTH, 140], fill=NAVY)

    # --- Green Bottom Banner ---
    draw.rectangle([0, HEIGHT-120, WIDTH, HEIGHT], fill=GREEN)
    draw.rectangle([0, HEIGHT-140, WIDTH, HEIGHT-120], fill=NAVY)

    # --- Corner Decorative Squares ---
    corner_size = 30
    for cx, cy in [(50, 150), (WIDTH-80, 150), (50, HEIGHT-180), (WIDTH-80, HEIGHT-180)]:
        draw.rectangle([cx, cy, cx+corner_size, cy+corner_size], fill=SAFFRON)
        draw.rectangle([cx+5, cy+5, cx+25, cy+25], fill=NAVY)

    # --- Load Fonts (falls back to default if system fonts unavailable) ---
    def load_font(size, bold=False):
        try:
            font_name = "arialbd.ttf" if bold else "arial.ttf"
            return ImageFont.truetype(font_name, size)
        except:
            return ImageFont.load_default()

    font_header_top = load_font(28, bold=True)
    font_title_big = load_font(72, bold=True)
    font_subtitle = load_font(32, bold=True)
    font_body = load_font(26)
    font_name = load_font(56, bold=True)
    font_score = load_font(36, bold=True)
    font_footer = load_font(20)

    # --- Top Banner Text ---
    draw.text((WIDTH//2, 40), "Government of India Initiative", font=font_header_top, fill="white", anchor="mm")
    draw.text((WIDTH//2, 85), "Atmanirbhar Bharat — Make in India", font=font_header_top, fill=GOLD, anchor="mm")

    # --- Main Title ---
    draw.text((WIDTH//2, 220), "Certificate of Achievement", font=font_subtitle, fill=NAVY, anchor="mm")

    # --- Decorative Horizontal Line ---
    draw.line([(100, 255), (WIDTH-100, 255)], fill=SAFFRON, width=3)
    draw.line([(100, 262), (WIDTH-100, 262)], fill=GREEN, width=2)

    # --- "SWADESHI QUEST" Game Title ---
    draw.text((WIDTH//2, 320), "SWADESHI QUEST", font=font_title_big, fill=NAVY, anchor="mm")
    draw.text((WIDTH//2, 390), "Journey Towards Atmanirbhar Bharat", font=font_body, fill=SAFFRON, anchor="mm")

    # --- "This Certifies That" ---
    draw.text((WIDTH//2, 460), "This certifies that", font=font_body, fill="#555555", anchor="mm")

    # --- Player Name (Highlighted) ---
    draw.text((WIDTH//2, 528), player_name, font=font_name, fill=NAVY, anchor="mm")

    # --- Underline under name ---
    name_bbox = draw.textbbox((0, 0), player_name, font=font_name)
    name_w = name_bbox[2] - name_bbox[0]
    draw.line([(WIDTH//2 - name_w//2, 560), (WIDTH//2 + name_w//2, 560)], fill=SAFFRON, width=3)

    # --- Achievement Text ---
    draw.text((WIDTH//2, 600), "has successfully completed all 5 levels and demonstrated", font=font_body, fill="#333333", anchor="mm")
    draw.text((WIDTH//2, 640), "exemplary knowledge of Indian Heritage, Culture & Swadeshi Values.", font=font_body, fill="#333333", anchor="mm")

    # --- Score Box ---
    draw.rounded_rectangle([WIDTH//2 - 180, 665, WIDTH//2 + 180, 715], radius=15, fill=LIGHT_SAFFRON, outline=SAFFRON, width=2)
    draw.text((WIDTH//2, 690), f"Final Score: {score} Points  |  Levels: {levels_completed}/5", font=font_score, fill=NAVY, anchor="mm")

    # --- Bottom Banner Text ---
    today = datetime.now().strftime("%d %B %Y")
    draw.text((200, HEIGHT-80), f"Date: {today}", font=font_footer, fill="white", anchor="mm")
    draw.text((WIDTH//2, HEIGHT-80), "Jai Hind 🇮🇳  |  Vocal for Local", font=font_footer, fill=GOLD, anchor="mm")
    draw.text((WIDTH-200, HEIGHT-80), "Swadeshi Quest v1.0", font=font_footer, fill="white", anchor="mm")

    # --- Save Certificate to Desktop ---
    desktop = os.path.join(os.path.expanduser("~"), "Desktop")
    safe_name = "".join(c if c.isalnum() else "_" for c in player_name)
    filename = os.path.join(desktop, f"SwadeshiQuest_Certificate_{safe_name}.png")
    img.save(filename)
    return filename
