<script>
import { Bar } from "vue-chartjs";

export default {
  extends: Bar,
  mounted() {
    this.renderChart(
      {
        labels: [
          "January",
          "February",
          "March",
          "April",
          "May",
          "June",
        ],
        datasets: [
          {
            label: "Data One",
            backgroundColor: "#55D8FB",
            data: [40, 20, 12, 39, 10, 41]
          }
        ]
      },
      { responsive: true, maintainAspectRatio: false }
    );
  }
};
</script>