function election() {
  const numOfCand = parseInt(prompt('How many candidates'));
  let candidates = [];

  for (let i = 0; i < numOfCand; i++) {
    let candidateInfo = {};
    let cName = prompt('Candidate number:' + i + ' name');
    candidateInfo['name'] = cName;
    candidateInfo['votes'] = 0;
    candidates.push(candidateInfo);
  }

  for (let j = 0; j < candidates.length; j++) {
    let vote = prompt('Who do you vote for: ' + candidates[j]['name']);
    for (let k = 0; k < candidates.length; k++) {
      if (candidates[k]['name'] === vote) {
        candidates[k]['votes']++;
      }
    }
  }
  for (let m = 0; m < candidates.length; m++) {
    console.log(candidates[m]['name'] + ' received ' + candidates[m]['votes'] +
        ' votes.');
  }
}
election()


