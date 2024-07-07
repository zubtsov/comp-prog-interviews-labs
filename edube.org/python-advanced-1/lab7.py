# https://edube.org/learn/python-advanced-1/lab

class LuxuryWatch:
    __watches_created = 0

    @classmethod
    def get_number_of_watches_created(cls):
        return cls.__watches_created

    @classmethod
    def with_engraving(cls, text: str):
        if len(text) > 40:
            raise ValueError("The engraving can't be longer than 40 characters")
        if not text.isalnum():
            raise ValueError("The engraving must contain only digits and letters")

        watch = LuxuryWatch()
        watch.engraving = text
        return watch

    def __init__(self):
        LuxuryWatch.__watches_created += 1


if __name__ == '__main__':
    watch1 = LuxuryWatch()
    watch2 = LuxuryWatch.with_engraving('engraving')
    try:
        watch3 = LuxuryWatch.with_engraving('foo@baz.com')
    except ValueError as e:
        print(e)
    print(LuxuryWatch.get_number_of_watches_created())
