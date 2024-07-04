const numSides = 12; // Ilość boków
const baseRadius = 1; // Promień podstawy

// Obliczanie współrzędnych wierzchołków podstawy 12-sto kąta foremnego
const baseVertices = [];
for (let i = 0; i < numSides; i++) {
    const theta = (i / numSides) * 2 * Math.PI;
    const x = baseRadius * Math.cos(theta);
    const z = baseRadius * Math.sin(theta);
    baseVertices.push([x, 0, z]);
}
console.log(baseVertices);
// Wysokość piramidy
const height = 1.5; // Przykładowa wysokość

// Wierzchołek piramidy
const apex = [0, height, 0];

// Łączenie współrzędnych podstawy i wierzchołka piramidy
const vertexPositions = baseVertices.flat().concat(apex);

// Definicja indeksów trójkątów
const indices = [];
for (let i = 0; i < numSides; i++) {
    indices.push(i, (i + 1) % numSides, numSides); // Boki podstawy
    indices.push(i, (i + 1) % numSides, numSides + 1); // Ściany piramidy
}

// Normalne wierzchołków - zakładając, że piramida jest zorientowana w górę
const vertexNormals = [];
for (let i = 0; i < baseVertices.length; i++) {
    vertexNormals.push(0, -1, 0); // Normalne podstawy
}

// Normalne boków
for (let i = 0; i < numSides; i++) {
    const v0 = baseVertices[i];
    const v1 = baseVertices[(i + 1) % numSides];
    const normal = [
        0,
        baseRadius,
        0
    ];
    vertexNormals.push(...normal, ...normal, ...normal); // Dla każdego boku podstawy trzy razy ta sama normalna
}
vertexNormals.push(0, 1, 0); // Normalne wierzchołka

const textureCoords = [];
for (let i = 0; i < baseVertices.length; i++) {
    const x = baseVertices[i][0] / (2 * baseRadius) + 0.5;
    const z = baseVertices[i][2] / (2 * baseRadius) + 0.5;
    textureCoords.push(x, z);
}
textureCoords.push(0.5, 0.5);

const piramida = {
    "vertexPositions": new Float32Array(vertexPositions),
    "vertexNormals": new Float32Array(vertexNormals),
    "vertexTextureCoords": new Float32Array(textureCoords),
    "indices": new Uint16Array(indices)
};