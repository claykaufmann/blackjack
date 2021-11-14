import * as React from 'react';
import Card from './Card';

const Player = (props) => {
  const data = props;
  const { cards, value, playerName } = data;

  return (
    <>
      <p>
        {playerName} hand value is {value}
      </p>
      {cards.map((card) => (
        <Card value={card[0]} suit={card[1]} visibility={card[2]} />
      ))}
    </>
  );
};

export default Player;
