from typing import Tuple, TypedDict
from django.http import HttpRequest
from django.shortcuts import render
from typing import NamedTuple


choices = ('Height', 'Weight', 'Width', 'Depth')
choices_set = {'Height', 'Weight', 'Width', 'Depth'}

nested_choices = (('Height', 'height'), ('Weight', 'weight'), ('Width', 'width'), ('Depth', 'depth'))

Formats = TypedDict("Formats", {
    'id': int,
    'display': str,
    'api_str': str,
})

choices_labeled: Tuple[Formats, Formats, Formats] = (
    {'id':0, 'api_str': 'height','display': 'Height'},
    {'id':1, 'api_str': 'weight','display': 'Weight'},
    {'id':2, 'api_str': 'depth','display': 'Depth'},
)




class LabeledChoice(NamedTuple):
    id: int
    display: str
    api_str: str

labeled_choices = [
    LabeledChoice(1, 'Height', 'height'),
    LabeledChoice(2, 'Weight', 'weight'),
    LabeledChoice(3, 'Depth', 'depth')
]


# Create your views here.
def enum_types(request: HttpRequest):

    param = request.GET.get("options")
    if param is None: raise TypeError("")

    ## Doesn't work
    # if param not in [choice.api_str for choice in labeled_choices]: raise TypeError("");

    ## Works good!
    if param not in choices: raise TypeError("");
    elif param == "Height": print()

    # Don't nest too hard
    # if param not in [choice[0] for choice in nested_choices]: raise TypeError("");
    # elif param == "

    # if param not in choices_set: raise TypeError("")
    # elif param == ""

    id = 2

    return render(
        request,
        'blog/index.html',
        {
            'choices':choices,
            'selected': choices[id]
        }
    )