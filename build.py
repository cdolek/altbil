import sys
import markdown
import codecs

if __name__ == "__main__":
    _, source_file, output_file = sys.argv;
    source = codecs.open(source_file, mode="r", encoding="utf-8")
    text = markdown.markdown(source.read())
    template = codecs.open("base.html", mode="r", encoding="utf-8")
    compiled = template.read().format(content=text)
    output = codecs.open(output_file, "w", encoding="utf-8", 
                         errors="xmlcharrefreplace")
    output.write(compiled)
