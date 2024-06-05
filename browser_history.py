'''
Can you implement a simplified version of a browser history tracker, that will keep track of
the order of visited pages (URLs), and will implement logic for visiting the previous, current
and following websites?

It should work like this:

We have an empty browser history
[]

Then we visit three websites in the following order: First we visit website A, then B, and then C.
Then our browsing history would look like this, having website C as the page we are currently
visiting:

[ A, B, C]
↑

If we "go back", or call the method back(), our current website would be B, our previous would be A,
 and the next one will be C.

[ A, B, C]
     ↑
Thus, by "going forward", or calling the method forward(), we would go to the website C again.

'''

class BrowserHistory:
    def __init__(self):
        self.history = []
        self.current = 0

    def visit(self, url):
        self.history = self.history[:self.current+1] + [url]
        self.current += 1

    def back(self):
        if self.current > 0:
            self.current -= 1
        return self.history[self.current]

    def forward(self):
        if self.current < len(self.history)-1:
            self.current += 1            
        return self.history[self.current]

