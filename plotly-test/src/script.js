const trace1 = {
    x: [1, 2, 3, 4],
    y: [10, 15, 13, 17],
    mode: 'markers'
};

const trace2 = {
    x: [2, 3, 4, 5],
    y: [16, 5, 11, 9],
    mode: 'lines'
};

const trace3 = {
    x: [1, 2, 3, 4],
    y: [12, 9, 15, 12],
    mode: 'lines+markers'
};

const data = [trace1, trace2, trace3];

const layout = {
    title: 'Line and Scatter Plot'
};

Plotly.newPlot('linePlotDiv', data, layout);

const barTrace1 = {
    x: ['giraffes', 'orangutans', 'monkeys'],
    y: [20, 14, 23],
    name: 'SF Zoo',
    type: 'bar'
};

const barTrace2 = {
    x: ['giraffes', 'orangutans', 'monkeys'],
    y: [12, 18, 29],
    name: 'LA Zoo',
    type: 'bar'
};

var barData = [barTrace1, barTrace2];

var barLayout = {barmode: 'group'};

Plotly.newPlot('barChartDiv', barData, barLayout);
