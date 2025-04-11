import os
import openai
import gradio as gr

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_post(topic):
    prompt = f"Напиши пост для Telegram-блога на тему: {topic}. Структура: заголовок, краткий подзаголовок, основной текст. Используй неформальный тон и реальные примеры."
    try:
        response = openai.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "Ты опытный копирайтер, создающий посты для Telegram-блога."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=1000
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Ошибка: {e}"

iface = gr.Interface(
    fn=generate_post,
    inputs=gr.Textbox(label="Тема поста"),
    outputs=gr.Textbox(label="Сгенерированный пост"),
    title="📝 Генератор постов для Telegram",
    description="Введите тему — получите пост, готовый к публикации."
)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    iface.launch(server_name="0.0.0.0", server_port=port)