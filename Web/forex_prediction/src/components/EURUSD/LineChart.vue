<script>
import { Line } from "vue-chartjs";

export default {
  extends: Line,
  data() {
  },
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
            label: "Predictline",
            data: [2, 10, 5, 9, 0, 6],
            backgroundColor: "transparent",
            borderColor: "#63dbff",
            pointBackgroundColor: "#63dbff"
          },
          {
            label: "Realline",
            data: [4, 12, 3, 7, 1, 5],
            backgroundColor: "transparent",
            borderColor: "#ffa8c4",
            pointBackgroundColor: "#ffa8c4"
          }
        ]
      },
      {
        responsive: true,
        maintainAspectRatio: false,
        title: {
          display: true,
          text: "My Data"
        }
      }
    );
  }
};
</script>