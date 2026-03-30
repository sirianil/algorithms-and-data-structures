'''
events = [
  {id:'D1', status:'accepted',  time:'10:00'},
  {id:'D2', status:'accepted',  time:'10:15'},  // D1 is in-flight → 1 concurrent
  {id:'D1', status:'delivered', time:'10:30'},
  {id:'D2', status:'cancelled', time:'10:45'},
]
base_rate=$10, bonus_rate=$5

D1 payout = $10 + 0 x $5 = $10
D2 payout = $10 + 1 x $5 = $15
Total = $25
'''

class DasherPayoutAPI:
    def __init__(self, events):
        self.events = events
        self.validate_events()
        self.calculate_concurrent_events()

    def calculate_concurrent_events(self):
        self.events = sorted(self.events, key=lambda x : x['time'])
        in_progress_event = 0
        self.concurrent_counts = {}

        for event in self.events:
            id = event['id']
            status = event['status']

            if status == 'accepted':
                self.concurrent_counts[id] = in_progress_event
                in_progress_event += 1                
            else:
                in_progress_event -= 1

    def get_base_rate(self):
        return 10
    
    def get_bonus(self):
        return 5

    def calculate_payout(self):
        total_payout = 0
        for event in self.events:
            if event['status'] == 'delivered' or event['status'] == 'cancelled':
                payout = self.get_base_rate() + (self.get_bonus() * self.concurrent_counts[event['id']])
                total_payout += payout
        return total_payout

if __name__ == '__main__':
    dasherPayoutAPI = DasherPayoutAPI([
    {'id':'D1', 'status':'accepted',  'time':'10:00'},
    {'id':'D2', 'status':'accepted',  'time':'10:15'},
    {'id':'D1', 'status':'delivered', 'time':'10:30'},
    {'id':'D2', 'status':'cancelled', 'time':'10:45'},
])
    print(dasherPayoutAPI.concurrent_counts)
    print(dasherPayoutAPI.calculate_payout())