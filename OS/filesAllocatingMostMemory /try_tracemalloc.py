import tracemalloc

import app

tracemalloc.start()

# app.run()

snapshot = tracemalloc.take_snapshot()
top_stats = snapshot.statistics("lineno")

for stat in top_stats[:10]:
    print(stat)

    print("😁")
