from django.views.generic import TemplateView

class HomePage(TemplateView):
    template_name='index.html'

class TestPage(TemplateView):
    template_name='test.html'

class ThanksPage(TemplateView):
    template_name='thanks.html'

class LinksPage(TemplateView):
    template_name='links.html'
 
class MessageBoard(TemplateView):
    template_name='message_board.html'

class Textbooks(TemplateView):
    template_name='textbooks.html'