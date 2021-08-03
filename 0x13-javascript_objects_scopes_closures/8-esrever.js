#!/usr/bin/node
export function esrever (list) {
    let i;
    const rev = [];
    for (i = list.length - 1; i >= 0; i--) {
      rev.push(list[i]);
    }
    return rev;
  }
