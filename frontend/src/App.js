import * as React from 'react';
import { useState } from 'react';
import logo from './logo.svg';
import './App.css';
// import Player from './components/Player';
import Card from './components/Card';

const App = () => {
  const [gameId, setGameId] = useState(0);

  // const [gameStatus, setGameStatus] = useState(false);
  const [playerCards, setPlayerCards] = useState([]);
  // const [dealerCards, setDealerCards] = useState([]);

  // const [playerValue, setPlayerValue] = useState(0);
  // const [dealerValue, setDealerValue] = useState(0);

  const [gameHasStarted, setGameStart] = useState(false);

  // TODO: remove this when further in development
  const [returnData, setReturnData] = useState('');

  const updateGameState = (data) => {
    setPlayerCards(data.player.cards);
    // setDealerCards(data.dealer.cards);

    // setPlayerValue(data.player.value);
    // setDealerValue(data.dealer.value);
  };

  const sendData = (event) => {
    event.preventDefault();

    fetch(`api/test_game/${gameId}`, {
      method: 'POST',
      type: 'JSON',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        test: 'Hi!',
        action: 'hit',
      }),
    })
      .then((res) => res.json())
      .then((data) => {
        setReturnData(data.game_id);
      });
  };

  // const sendAction = (event) => {
  //   event.preventDefault();

  //   // api call here
  // };

  const gameStart = (event) => {
    // check if the game has already started
    if (gameHasStarted) {
      return;
    }

    event.preventDefault();

    fetch('/api/start')
      .then((res) => res.json())
      .then((data) => {
        setGameId(data.game_id);
        // setGameStatus(true);

        // set game status
        updateGameState(data);
      });

    setGameStart(true);
  };

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>The game ID is {gameId}</p>
        {gameHasStarted ? (
          <div>
            <button type="button" onClick={sendData}>
              Send Data!
            </button>

            {/* <Player value={dealerValue} cards={dealerCards} />
            <Player value={playerValue} cards={playerCards} /> */}

            <Card value={playerCards[0].value} />

            <p>{returnData}</p>
          </div>
        ) : (
          <button type="button" onClick={gameStart}>
            Start Game!
          </button>
        )}
      </header>
    </div>
  );
};

export default App;
