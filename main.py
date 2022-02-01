from add_and_remove import AddRemove


class CountrySearch(AddRemove):

    f = 'memory.txt'

    def search(self, query):
        response = []
        for country in self.name_county:
            if query in country:
                response.append(country)
        return response
    
country = CountrySearch()
print(county)

# test
