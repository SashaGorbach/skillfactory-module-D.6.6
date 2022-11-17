from django import template

register = template.Library()

# Регистрируем наш фильтр под именем currency, чтоб Django понимал,
# что это именно фильтр для шаблонов, а не простая функция.


bad_words = ['редиска', 'попа', 'жопа']

@register.filter()
def bad_words_hide(text):
   list_words_text = []
   list_words_text = text.split(' ')
   for i in range(len(list_words_text)):
      if list_words_text[i].lower() in bad_words:
         list_words_text[i] = list_words_text[i][:1] + (len(list_words_text[i]) - 1) * '*'

   text = " ".join(list_words_text)
   return text