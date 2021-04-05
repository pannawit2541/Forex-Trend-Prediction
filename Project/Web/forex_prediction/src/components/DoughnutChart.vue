<template>
  <div id="donut">
    <div id="chart" style="width: 200px; height: 50px; min-height: 100px;">
      <apexchart
        type="radialBar"
        width="200"
        :options="this.chartOptions"
        :series="series"
        
      ></apexchart>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      series: this.series_percent,
      chartOptions: {
        chart: {
          type: "radialBar",
        },
        plotOptions: {
          radialBar: {
            offsetX: -26,
            offsetY: -20,
            dataLabels: {
              name: {
                show: false,
              },
              value: {
                color: "#000000",
                fontFamily: "Nunito Sans",
                fontWeight: "bold",
                fontSize: "20px",
                offsetY: 8,
              },
            },
            hollow: {
              margin: 2,
            },
          },
        },
        fill: {
          colors: this.fill_color,
        },
        stroke: {
          lineCap: "round",
        },
      },
    };
  },
  props: {
    series_percent: Array,
    fill_color: String,
  },
};
</script>

<style scoped>
@import url("https://fonts.googleapis.com/css?family=Nunito+Sans");

#donut {
  font-family: "Nunito Sans";
}
</style>
