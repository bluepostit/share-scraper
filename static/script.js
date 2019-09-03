function fetchBrandShareData(searchTerm) {
  url = "/search?term=" + encodeURIComponent(searchTerm);
  return fetch(url)
  .then(response => response.json())
  .then((json) => {
    console.log(json);
    let chartData = buildChartData(json);
    let title = `Brand shares for "${json.searchTerm}"`
    showDataInChart(chartData, title);
  });
}

function buildChartData(data) {
  const chartData = {
    labels: data.brands,
    datasets: []
  };
  backgroundColors = [
  'rgba(54, 162, 235, 0.2)',
  'rgba(75, 192, 192, 0.2)'
  ];
  borderColors = [
  'rgba(54, 162, 235, 1)',
  'rgba(75, 192, 192, 1)'
  ];
  let i = 0;
  for (let share of data.shares) {
    const provider = share.provider;
    const shares = share.shares;
    let dataset = {
      label: `${provider} brand share %`,
      data: shares,
      backgroundColor: backgroundColors[i],
      borderColor: borderColors[i],
      borderWidth: 1
    };
    chartData.datasets.push(dataset);
    i++;
  }
  return chartData;
}

function showDataInChart(data, title) {
  let ctx = document.getElementById('chart').getContext('2d');
  let chart = new Chart(ctx, {
    type: 'horizontalBar',
    data: data,
    options: {
      responsive: true,
      legend: {
        position: 'left',
      },
      title: {
        display: true,
        text: title
      },
      barThickness: 2,
    }
  });
}

const setupFormListener = () => {
  document.querySelector('.search-form').addEventListener('submit', e => {
    e.preventDefault();
    const searchTerm = document.querySelector('#search-term').value;
    fetchBrandShareData(searchTerm);
  });
};

const setupChartConfig = () => {
  Chart.scaleService.updateScaleDefaults('linear', {
    ticks: {
      min: 0,
      max: 100
    }
  });
};

document.addEventListener("DOMContentLoaded", function(event) {
  setupFormListener();
  setupChartConfig();
});
