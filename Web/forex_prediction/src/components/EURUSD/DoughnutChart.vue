<template>
  <div id="donut">
    <div id="chart">
      <apexchart
        type="radialBar"
        width="180"
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
      series: [70],
      chartOptions: {
        chart: {
          type: "radialBar",
        },
        plotOptions: {
          radialBar: {
            offsetX: -30,
            offsetY: -10,
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
          colors: "#FFA7C4",
        },
        stroke: {
          lineCap: "round",
        },
      },
    };
  },
};
</script>

<style scoped>
@import url("https://fonts.googleapis.com/css?family=Nunito+Sans");

#donut {
  font-family: "Nunito Sans";
}
</style>
