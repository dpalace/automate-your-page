def generate_concept_HTML(concept_title, concept_description):
    html_text_1 = '''
    <div class="concept">
        <div class="concept-title">
            ''' + concept_title
    html_text_2 = '''
        </div>
        <div class="concept-description">
            ''' + concept_description
    html_text_3 = '''
        </div>
    </div>'''
    
    full_html_text = html_text_1 + html_text_2 + html_text_3
    return full_html_text

first_concept = 'Internet'
first_description = 'A global network of computers that connects billions of users worldwide.'

second_concept = 'Function'
second_description = 'Something that takes input, does something to that input, and then produces output.'

print generate_concept_HTML(first_concept, first_description)
print generate_concept_HTML(second_concept, second_description)
