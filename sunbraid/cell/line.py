import uuid
def make_lineplot(data, height=50):
    random_id = str(uuid.uuid4()).replace('-', '')
    return f"""
    <div class="chart-container">
        <div id="rdivRUID{random_id}"></div>
    </div>
    <script>
        const dataRUID{random_id} = {data};
        createLinePlot(dataRUID{random_id},  'rdivRUID{random_id}', {height});
    </script>
"""