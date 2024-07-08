+++
title = "Is the {{template_data.gpu_name}} GPU good enough for Blender in 2024?"
date = "2024-04-07"
+++

If you're planning on rendering complex Blender scenes, you might be wondering if your computer is up to the task. In this post we will explore wether or not the **{{template_data.gpu_name}}** GPU is sufficient.

To start off, we will look at benchmark data to compare the GPU with other common GPUs. We will use [3DMark](https://benchmarks.ul.com/3dmark) benchmark results.

The **{{template_data.gpu_name}}** GPU received a 3DMark score of **{{template_data.score}}**. Here's how it compares to other common GPUs.

![](comparison.svg)

The benchmark shows a performance of {{template_data.percentage}}% that of the GeForce RTX 4090, the currently fastest GPU on the market.

# Render time comparison

Now we will compare the time it takes to render different sample scenes by GPU. We will compare these results with our RenderFarm, in case you need your renders to finish quickly.

## Classroom scene
<video src="../classroom.mp4" width="100%" controls></video>

<table>
  <tr>
    <th>GPU</th>
    <th>Rendering Time</th>
  </tr>
  <tr>
    <td style="padding: 0 15px 0 0;">{{template_data.gpu_name}}</td>
    <td>{{template_data.classroom_render_time_current}}</td>
  </tr>
  <tr>
    <td style="padding: 0 15px 0 0;">GeForce GTX 1080</td>
    <td>{{template_data.classroom_render_time_gtx_1080}}</td>
  </tr>
  <tr>
    <td style="padding: 0 15px 0 0;">GeForce RTX 2060</td>
    <td>{{template_data.classroom_render_time_rtx_2060}}</td>
  </tr>
  <tr>
    <td style="padding: 0 15px 0 0;">GeForce RTX 4090</td>
    <td>{{template_data.classroom_render_time_rtx_4090}}</td>
  </tr>
  <tr>
    <td style="padding: 0 15px 0 0;"><a href="https://renderlab.io">RenderLab.io</a></td>
    <td>{{template_data.classroom_render_time_renderlab}} for <b>{{template_data.classroom_price_renderlab}}</b></td>
  </tr>
</table>
<br><br>

## Architecture scene
<video src="../architecture.mp4" width="100%" controls></video>

<table>
  <tr>
    <th>GPU</th>
    <th>Rendering Time</th>
  </tr>
  <tr>
    <td style="padding: 0 15px 0 0;">{{template_data.gpu_name}}</td>
    <td>{{template_data.architecture_render_time_current}}</td>
  </tr>
  <tr>
    <td style="padding: 0 15px 0 0;">GeForce GTX 1080</td>
    <td>{{template_data.architecture_render_time_gtx_1080}}</td>
  </tr>
  <tr>
    <td style="padding: 0 15px 0 0;">GeForce RTX 2060</td>
    <td>{{template_data.architecture_render_time_rtx_2060}}</td>
  </tr>
  <tr>
    <td style="padding: 0 15px 0 0;">GeForce RTX 4090</td>
    <td>{{template_data.architecture_render_time_rtx_4090}}</td>
  </tr>
  <tr>
    <td style="padding: 0 15px 0 0;"><a href="https://renderlab.io">RenderLab.io</a></td>
    <td>{{template_data.architecture_render_time_renderlab}} for <b>{{template_data.architecture_price_renderlab}}</b></td>
  </tr>
</table>
<br><br>


Are you looking to speed up your renders? [RenderLab.io](https://renderlab.io) currently offers free Cycles renders for new users. No strings attached!