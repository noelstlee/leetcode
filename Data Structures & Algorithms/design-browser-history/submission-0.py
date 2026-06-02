class ListNode:
    def __init__(self, url, prev=None, next=None):
        self.url = url
        self.prev = prev
        self.next = next

class BrowserHistory:

    def __init__(self, homepage: str):
        """
        None <- HEAD -> <- homepage <- -> TAIL -> None
        """
        self.currPage = ListNode(homepage)
        

    def visit(self, url: str) -> None:
        """
        Visits url from the current page. It clears up all the forward history.
        """
        self.currPage.next = ListNode(url, prev=self.currPage)
        self.currPage = self.currPage.next


    def back(self, steps: int) -> str:
        """
        Move steps back in history. 
        If you can only return x steps in the history and steps > x, 
        you will return only x steps. 
        Return the current url after moving back in history at most steps.
        """
        while self.currPage.prev and steps > 0:
            self.currPage = self.currPage.prev
            steps -= 1
        return self.currPage.url


    def forward(self, steps: int) -> str:
        """
        Move steps forward in history. 
        If you can only forward x steps in the history and steps > x, 
        you will forward only x steps. 
        Return the current url after forwarding in history at most steps.
        """
        while self.currPage.next and steps > 0:
            self.currPage = self.currPage.next
            steps -= 1
        return self.currPage.url

        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)