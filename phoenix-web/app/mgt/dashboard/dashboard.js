import {syncApiResolve, asyncApiResolve} from "../../../common/utils.js";
import {urls} from "../../../config/urls.js";

// 初始化日历
const initialCalendar = () => {
    layui.laydate.render({
        elem: "#calendar",
        value: new Date(),  // 填充初始值为当前日期
        position: "static",  // 静态显示
        showBottom: false,  // 关闭底部按钮
        calendar: true,  // 显示公历节日
    })
}

const initialStatisticData = () => {
    const successCallback = (res) => {
        layui.jquery("#dashboardArticleCount").empty().text(res.data[0].article_count)
        layui.jquery("#dashboardCommentCount").empty().text(res.data[0].comment_count)
        layui.jquery("#dashboardTagCount").empty().text(res.data[0].tags_count)
        layui.jquery("#dashboardAccessCount").empty().text(res.data[0].access_count)
        layui.jquery("#dashboardUnpublishArticleCount").empty().text(res.data[0].unpublish_count)
        layui.jquery("#dashboardFlinkCount").empty().text(res.data[0].flink_apply)
        layui.jquery("#dashboardFansCount").empty().text(res.data[0].fans_count)
    }
    asyncApiResolve(urls.dashboardStatistic, null, 'get', successCallback);
}

const initialCarousel = () => {
    layui.carousel.render({
        elem: "#dashboardCarousel",
        width: '100%',
        autoplay: false,
        height: '350px',
        // indicator: 'outside',
        trigger: 'hover',
        arrow: 'none',
    })
}

// 堆叠区域折线图
const stackAreaLineCharts = () => {
    const charts = echarts.init(document.getElementById("accessStackAreaCharts"))
    let response = syncApiResolve(urls.dashboardAccessCharts)

    let option = {
        title: {
            text: '访问记录',
            x: 'center',
            y: '10px',
            textAlign: 'center',
            textStyle: {
                fontSize: 15,
                fontWeight: 500,
                fontFamily: 'Microsoft YaHei',
            },
        },
        grid: {
            show: true,
        },
        tooltip: {
            trigger: 'axis',
            axisPointer: {
                type: 'line',
                label: {
                    backgroundColor: '#009688'
                }
            }
        },
        xAxis: {
            type: 'category',
            boundaryGap: false,
            data: response.data.map(obj => {return obj.date}),
            axisLine: {
                color: '#009688'
            }
        },
        yAxis: {
            type: 'value',
            axisLine: {
                show: true,
                lineStyle: {
                    color: '#009688'
                }
            }
        },
        series: {
            name: '访问总量',
            type: 'line',
            stack: '总量',
            areaStyle: {
                color: '#009688'
            },
            lineStyle: {
                color: '#009688'
            },
            data: response.data.map(obj => {return obj.count})
        },
    };
    charts.setOption(option)
}

const articleBarChart = () => {
    const chart = echarts.init(document.getElementById('articlePublishCharts'))
    const response = syncApiResolve(urls.dashboardArticleChart)

    let option = {
        title: {
            text: '博文记录',
            x: 'center',
            y: '10px',
            textAlign: 'center',
            textStyle: {
                fontSize: 15,
                fontWeight: 500,
                fontFamily: 'Microsoft YaHei',
            },
        },
        color: ['#3398DB'],
        tooltip: {
            trigger: 'axis',
            axisPointer: {            // 坐标轴指示器，坐标轴触发有效
                type: 'shadow'        // 默认为直线，可选为：'line' | 'shadow'
            }
        },
        xAxis: {
            type: 'category',
            data: response.data.map(obj => {return obj.date}),
            axisTick: {
                alignWithLabel: true
            }
        },
        yAxis: {
            type: 'value'
        },
        series: {
            name: '创建博文',
            type: 'bar',
            barWidth: '40%',
            data: response.data.map(obj => {return obj.count}),
        }
    };
    chart.setOption(option)
}

const resizeCharts = (elemID) => {
    const chart = echarts.init(document.getElementById(elemID))
    chart.resize()
}

const initialProcess = () => {
    const response = syncApiResolve(urls.dashboardProcessData)
    const articlePercent = `${response.data[0].article_update_rate}%`
    const taskPercent = `${response.data[0].task_incomplete_rate}%`
    layui.element.progress('articleUpdateRate', articlePercent)
    layui.jquery('#articleUpdateRate').attr('lay-percent', articlePercent);
    layui.element.progress('taskIncompleteRate', taskPercent)
    layui.jquery('#taskIncompleteRate').attr('lay-percent', taskPercent);
    layui.element.init()
}

const initialPlanTaskTable = () => {
    layui.table.render({
        elem: '#emergencyTaskTable',
        url: urls.projectTaskListApi,
        where: {
            status: 'plan',
            priority: '1',
        },
        id: 'emergencyTaskTable',
        limit: 10,
        text: {
            none: "暂无相关数据",
        },
        cols: [[
            {field: 'project_name', title: '所属项目', align: "center", width: 90},
            {field: 'name', title: '任务', align: "center", width: 181, templet: (obj)=>{
                return `<span style="color: #F4516C">${obj.name}</span>`
                }},
            {field: 'ctime', title: '创建时间', align: "center", width: 102, templet: (obj)=> {
                return obj.ctime.split(' ')[0]
                }},
        ]]
    })
}

const initialRecentCommentTable = () => {
    layui.table.render({
        elem: '#recentCommentTable',
        url: urls.commentListApi,
        id: 'recentCommentTable',
        limit: 10,
        text: {
            none: "暂无相关数据",
        },
        cols: [[
            {field: 'nickname', title: '评论人', align: "center", templet: (obj)=>{
                return `<span style='color: #5AB1EF'>${obj.nickname}</span>`
                }},
            {field: 'email', title: '邮箱', align: "center"},
            {field: 'content', title: '评论', align: "center", templet: (obj)=>{
                return `<span style='color: #6CC8C1'>${obj.content}</span>`
                }},
            {field: 'ctime', title: '评论时间', align: "center"},
        ]]
    })
}

// 页面加载完毕后的动态操作
layui.jquery(document).ready(() => {
    // 渲染紧急任务表格
    initialPlanTaskTable();

    // 加载统计数据
    initialStatisticData();

    // 渲染轮播图
    initialCarousel();

    // 渲染访问记录堆叠区域折线图
    stackAreaLineCharts();

    // 渲染文章发表柱状图
    articleBarChart();

    // 加载事件进度
    initialProcess();

    // 渲染日历
    initialCalendar();

    // 渲染最近评论表
    initialRecentCommentTable();

    // 轮播图切换时，重载charts图表
    layui.carousel.on('change(dashboardCarousel)', function (obj) {
        resizeCharts(obj.item.attr('id'))
    })
})