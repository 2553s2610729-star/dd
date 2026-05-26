import streamlit as st
from PIL import Image, ImageEnhance, ImageDraw, ImageFont
import io

st.set_page_config(page_title="인스타 사진 꾸미기", page_icon="📸")

st.title("📸 인스타 사진 꾸미기")

uploaded_file = st.file_uploader(
    "사진 업로드",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:

    # 이미지 열기
    image = Image.open(uploaded_file).convert("RGB")

    st.subheader("원본 사진")
    st.image(image, use_container_width=True)

    # 필터 선택
    filter_type = st.selectbox(
        "필터 선택",
        ["기본", "밝게", "빈티지", "강한 대비"]
    )

    edited = image.copy()

    # 필터 적용
    if filter_type == "밝게":
        brightness = ImageEnhance.Brightness(edited)
        edited = brightness.enhance(1.3)

    elif filter_type == "빈티지":
        color = ImageEnhance.Color(edited)
        edited = color.enhance(0.7)

        contrast = ImageEnhance.Contrast(edited)
        edited = contrast.enhance(0.9)

    elif filter_type == "강한 대비":
        contrast = ImageEnhance.Contrast(edited)
        edited = contrast.enhance(1.8)

    # 텍스트 추가
    text = st.text_input("사진에 넣을 문구")

    if text:
        draw = ImageDraw.Draw(edited)

        width, height = edited.size

        draw.text(
            (30, height - 60),
            text,
            fill="white"
        )

    st.subheader("꾸며진 사진")
    st.image(edited, use_container_width=True)

    # 다운로드 버튼
    buffer = io.BytesIO()
    edited.save(buffer, format="PNG")

    st.download_button(
        label="📥 사진 다운로드",
        data=buffer.getvalue(),
        file_name="instagram_photo.png",
        mime="image/png"
    )
