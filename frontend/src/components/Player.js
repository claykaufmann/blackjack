import * as React from 'react';
import Card from './Card';

const Player = (props) => {
  const data = props;
  const { cards, value, playerName } = data;

  return (
    <div className="Player">
      <p>
        {playerName} hand value is {value}
      </p>
      <div className="Player-cards">
        {cards.map((card) => (
          <Card value={card[0]} suit={card[1]} visibility={card[2]} />
        ))}
      </div>
    </div>
  );
};

export default Player;
