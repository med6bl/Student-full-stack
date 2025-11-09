from rest_framework.decorators import api_view
from rest_framework.response import Response
from transformers import pipeline


summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
translator_en_fr = pipeline("translation_en_to_fr", model="Helsinki-NLP/opus-mt-en-fr")
translator_fr_en = pipeline("translation_fr_to_en", model="Helsinki-NLP/opus-mt-fr-en")
translator_en_ar = pipeline("translation_en_to_ar", model="Helsinki-NLP/opus-mt-en-ar")
translator_ar_en = pipeline("translation_ar_to_en", model="Helsinki-NLP/opus-mt-ar-en")

@api_view(['POST'])
def summarize_view(request):
    text = request.data.get('text', '')
    if not text:
        return Response({"error": "No text provided"}, status=400)

    try:
        summary = summarizer(text, max_length=120, min_length=30, do_sample=False)
        return Response({"summary": summary[0]['summary_text']})
    except Exception as e:
        return Response({"error": str(e)}, status=500)


@api_view(['POST'])
def translate_view(request):
    text = request.data.get('text', '')
    target = request.data.get('target', 'French').lower()

    if not text:
        return Response({"error": "No text provided"}, status=400)

    try:
        if target == "french":
            translation = translator_en_fr(text)[0]['translation_text']
        elif target == "english":
            # Guess if source is French or Arabic
            if any(ord(c) > 127 for c in text):  # crude Arabic/French detection
                if 'ال' in text or 'و' in text:
                    translation = translator_ar_en(text)[0]['translation_text']
                else:
                    translation = translator_fr_en(text)[0]['translation_text']
            else:
                translation = "Input already in English"
        elif target == "arabic":
            translation = translator_en_ar(text)[0]['translation_text']
        else:
            translation = "Unsupported language. Try English, French, or Arabic."
        return Response({"translation": translation})
    except Exception as e:
        return Response({"error": str(e)}, status=500)
