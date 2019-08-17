import React from 'react';
import logo from './logo.svg';
import './App.css';

class App extends React.Component {

    state = {
        players: []
    };

    componentDidMount() {
        fetch('https://gist.githubusercontent.com/OskarKaminski/a3f11650fbf83831521cadeb5d175deb/raw/2970163bf0d793068720e99caa326882b0dbc49d/players.json').then((res) => {
            return res.json()
        }).then((data) => {
            console.log(data);
            this.setState(
                {
                    players: data
                }
            )
        })
    }

    render() {
        if (this.state.players.length > 0) {
            return (
                <div className="App">
                    <header className="App-header">
                        {
                            this.state.players.map((player) => (
                                <div className="player" key={player.name}>
                                    <p>{player.name}</p>
                                    <div className="cards">
                                        {
                                            player.cards.map((card, i) => (
                                                <div className="card" key={i}>
                                                    {card.value} {card.suit}
                                                </div>
                                            ))
                                        }
                                    </div>
                                </div>
                            ))
                        }
                    </header>
                </div>
            )
        }
        return null;
    }
}

export default App;
