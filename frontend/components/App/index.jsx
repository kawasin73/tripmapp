import React from 'react'
import SearchBar from 'material-ui-search-bar'

export default function () {
  return (
    <div>
      <SearchBar
        onChange={(value) => console.log('onChange' + value)}
        onRequestSearch={(value) => console.log('onRequestSearch' + value)}
        style={{
          margin: '0 auto',
          maxWidth: 800
        }}
      />
      <p>Hello World</p>
      <p>Hello World2</p>
    </div>
  )
}
