from rest_framework.renderers import XMLRenderer
from six import StringIO
from django.utils.xmlutils import SimplerXMLGenerator

class CustomXMLRenderer(XMLRenderer):
    def render(self, data, accepted_media_type=None, renderer_context=None):
        """
        Renders `data` into serialized XML without the root tag
        """
        if data is None:
            return ''

        stream = StringIO()

        xml = SimplerXMLGenerator(stream, self.charset)
        xml.startDocument()
        #xml.startElement("root", {})

        self._to_xml(xml, data)

        #xml.endElement("root")
        xml.endDocument()
        return stream.getvalue()

