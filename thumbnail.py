def title(t, output_dir="."):  # 기본 저장 경로는 현재 폴더
    site = "프로그래머스"
    title_text = t[2:]
    language = "MySQL"
    text = (f"{{{site}}}\n{title_text}\n[언어 : {language}]")

    # 이미지 설정
    img_size = (800, 800)
    background_color = (0, 0, 0)
    text_color = (0, 255, 255)
    font_size = 50
    line_spacing = 20

    img = Image.new("RGB", img_size, background_color)
    draw = ImageDraw.Draw(img)

    font_path = "C:/Windows/Fonts/malgun.ttf"
    font = ImageFont.truetype(font_path, font_size)

    lines = text.split('\n')
    max_width = 0
    total_height = 0
    line_heights = []

    for line in lines:
        bbox = draw.textbbox((0, 0), line, font=font)
        width = bbox[2] - bbox[0]
        height = bbox[3] - bbox[1]
        max_width = max(max_width, width)
        total_height += height + line_spacing
        line_heights.append(height)
    total_height -= line_spacing

    x = (img_size[0] - max_width) / 2
    y = (img_size[1] - total_height) / 2

    for i, line in enumerate(lines):
        draw.text((x, y), line, fill=text_color, font=font)
        y += line_heights[i] + line_spacing

    # ⬇ 이미지 저장 경로 설정
    output_image_path = os.path.join(output_dir, f"{title_text}.png")
    img.save(output_image_path)
    print(f"✅ 이미지가 생성되었습니다: {output_image_path}")
