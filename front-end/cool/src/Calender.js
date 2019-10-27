import React from 'react';
import './Calender.css';
class Calender extends React.Component {
  constructor(props) {
    super(props);
  }

  getSunday(d) {
    d = new Date(d);
    var day = d.getDay();
    var diff = d.getDate() - day + (day == 0 ? -6:1); // adjust when day is sunday
    return new Date(d.setDate(6+diff));
  }

  getMonday(d) {
    d = new Date(d);
    var day = d.getDay();
    var diff = d.getDate() - day + (day == 0 ? -6:1); // adjust when day is sunday
    return new Date(d.setDate(diff));
  }

  getblocks = (i) => {
      return (
        <tr>
            <td className="cell">{i}</td>
            <td className="cell">{i}</td>
            <td className="cell">{i}</td>
            <td className="cell">{i}</td>
            <td className="cell">{i}</td>
            <td className="cell">{i}</td>
            <td className="cell">{i}</td>
        </tr>
      )
  }

  getRows = () => {
      var trs = [];
      var i;
      for(i = 0; i<48; i++){
          trs.push(this.getblocks(i));
      }
      return (
        <table>
            { trs }
        </table>
      )
  }


  render() {
    var monday = this.getMonday(this.props.today);
    fetch('http://localhost:5000/get_calendar?name='+this.props.communityName+'&year='+monday.getFullYear().toString()+'&month='+monday.getMonth().toString()+'&day='+monday.getDate().toString())
    .then(result => {
      return result.json();
    }).then(data => {
      console.log(data);
    })
    return (
      <div className="Calender-container">
        { this.getRows() }
      </div>
    );
  }
}

export default Calender;
