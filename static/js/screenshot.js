document.getElementById('download-btn').addEventListener('click', function () {
    const element = document.getElementById('project');

    html2canvas(element).then(canvas => {
        const image = canvas.toDataURL('image/png');

        const link = document.createElement('a');
        link.href = image;
        link.download = 'project.png';

        link.click();
    });
});