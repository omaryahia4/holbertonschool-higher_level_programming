#!/usr/bin/node
export function callMeMoby (num, theFunction) {
    for (let i = 0; i < num; i++) {
      theFunction();
    }
  }
