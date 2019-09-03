(() => {
  function fetchBrandShareData(searchTerm) {
    url = "/search?term=" + encodeURIComponent(searchTerm);
    return fetch(url)
      .then(response => response.json())
      .then((json) => {
        let chartData = buildChartData(json);
        let count = json.resultsCount;
        let title = `Brand shares for "${json.searchTerm}" (top ${count} results)`;
        document.querySelector('.msg-no-data').style.display = 'none';
        showDataInChart(chartData, title);
      });
  }

  function buildChartData(data) {
    const chartData = {
      labels: data.brands,
      datasets: []
    };
    backgroundColors = [
    'rgba(54, 162, 235, 0.9)',
    'rgba(75, 192, 192, 0.9)'
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

  function setFormInputsEnabled(flag) {
    document.querySelectorAll('.search-form input').forEach(element => {
      if (!!flag) {
        element.removeAttribute('disabled');
      } else {
        element.setAttribute('disabled', '');
      }
    });
  }

  function showLoading(flag) {
    setFormInputsEnabled(!flag);
    showLoadingSpinner(!!flag);
  }


  function showLoadingSpinner(flag) {
    const spinner = document.querySelector('.spinner-loading');
    if (!!flag) {
      spinner.style.display = 'block';
    } else {
      spinner.style.display = 'none';
    }
  }

  const setupFormListener = () => {
    document.querySelector('.search-form').addEventListener('submit', e => {
      e.preventDefault();
      const textInput = document.querySelector('#search-term');
      const searchTerm = textInput.value.trim();
      if (searchTerm == '') {
        alert('Please enter a search term');
        return;
      }
      showLoading(true);
      fetchBrandShareData(searchTerm)
        .then(() => {
          showLoading(false);
          textInput.value = '';
        });
    });
  };

  const setupChartConfig = () => {
    Chart.scaleService.updateScaleDefaults('linear', {
      ticks: {
        min: 0
      }
    });
  };

  document.addEventListener("DOMContentLoaded", function(event) {
    setupFormListener();
    setupChartConfig();
  });
})();