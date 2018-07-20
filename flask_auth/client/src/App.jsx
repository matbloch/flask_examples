import React from 'react';
import axios from 'axios';

// const AUTH_API_ENDPOINT = "http://0.0.0.0:8080/api/login";
const AUTH_API_ENDPOINT = "/api/login";

class App extends React.Component {


    constructor(props) {
      super(props);
      this.state = {
          status: 0,
          response: ""
      };
    }


    getAuthToken = () => {
        axios.post(AUTH_API_ENDPOINT, {
            "username": "mat",
            "password": "123"
          })
          .then((response) => {
            console.log(response);
            this.setState({status: response.status, response: JSON.stringify(response.data)});

          })
          .catch( (error) => {
              console.log(error.message);
              console.log(error.response);

              this.setState({status: error.status, response: JSON.stringify(error.data)});
              console.log(error.statusText);
            console.log(error);
          });

        // Make a request for a user with a given ID
        // axios({
        //       method:'post',
        //       url:AUTH_API_ENDPOINT,
        //       data: {
        //         firstName: 'Fred',
        //         lastName: 'Flintstone'
        //       }
        //     })
        //   .then(function (response) {
        //     // handle success
        //     console.log(response);
        //   })
        //   .catch(function (error) {
        //     // handle error
        //     console.log(error);
        //     console.log(error.reponse);
        //     console.log(error.message);
        //   })
        //   .then(function () {
        //     // always executed
        //   });
    }

    componentDidMount = () => {
        console.log("mounted");
        this.getAuthToken();
    }

    render() {
        return (
            <div>
                <strong>API Request on component load:</strong>
                <ul>
                    <li>Request Status: {this.state.status}</li>
                    <li>Response: {this.state.response}</li>
                </ul>
            </div>
        );
    }
}

export default App;
