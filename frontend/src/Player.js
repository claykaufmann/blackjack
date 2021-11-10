import * as React from 'react';

const Player = (value, cards) => {

  

  return (
    <>
      {for loop here for cards}
      <Card value={cards.value} suit={cards.suit} />
    </>
  );
};

export default Player;
