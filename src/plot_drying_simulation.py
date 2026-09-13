import numpy as np
import matplotlib.pyplot as plt
import os

# ===================== Global plot settings (academic style) =====================
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['figure.dpi'] = 300
plt.rcParams['font.size'] = 10
FIG_SAVE_DIR = "./output_figs"
os.makedirs(FIG_SAVE_DIR, exist_ok=True)

# ===================== Simulation data (replace with your real data) =====================
# Time series
t = np.linspace(0, 14000, 500)
T_oven = 28 + 22 * (1 - np.exp(-t / 2500))
mc_center = 0.48 * np.exp(-t / 3200)

# Radial coordinate
r = np.linspace(0, 1, 200)
T_rad_3h = 32 + 16 * (1 - r**2)
mc_rad_6h = 0.32 * (1 - 0.4 * r**1.5)

# Shrinkage model
mc_shrink = np.linspace(0.1, 0.5, 100)
radius_shrink = 0.8 + 0.2 * mc_shrink

# Convergence residual
iter_num = np.arange(1, 200)
residual = 0.08 * np.exp(-iter_num / 45)

# 2D grid for spatial contour plots
nx, ny = 100, 100
x = np.linspace(-1, 1, nx)
y = np.linspace(-1, 1, ny)
X, Y = np.meshgrid(x, y)
R2 = X**2 + Y**2
# Temperature field
T_2d = 30 + 18 * np.exp(-R2 / 0.6)
# Moisture field
mc_2d = 0.42 * np.exp(-R2 / 0.8)

# ===================== Plot Group 1 =====================
def plot_group1():
    # fig1_1
    fig, ax = plt.subplots(figsize=(6,4))
    ax.scatter(t, T_oven, s=2, label="原始采样点")
    ax.plot(t, T_oven, c="orange", lw=1.5, label="线性插值曲线")
    ax.set_xlabel("时间 (s)")
    ax.set_ylabel("烘房温度 (℃)")
    ax.legend()
    ax.grid(alpha=0.3)
    plt.tight_layout()
    plt.savefig(f"{FIG_SAVE_DIR}/fig1_1_temp_preprocess.png")
    plt.close()

    # fig1_2
    fig, ax = plt.subplots(figsize=(6,4))
    ax.plot(t, mc_center, c="#2ca02c")
    ax.set_xlabel("时间 (s)")
    ax.set_ylabel("含水率")
    ax.grid(alpha=0.3)
    plt.tight_layout()
    plt.savefig(f"{FIG_SAVE_DIR}/fig1_2_moisture_conc.png")
    plt.close()

    # fig1_3 material temperature spatial contour
    fig, ax = plt.subplots(figsize=(5,4))
    cf = ax.contourf(X,Y,T_2d, cmap="RdYlBu_r", levels=20)
    plt.colorbar(cf, ax=ax, label="温度 ℃")
    ax.set_title("物料温度场分布")
    ax.set_aspect("equal")
    plt.tight_layout()
    plt.savefig(f"{FIG_SAVE_DIR}/fig1_3_material_temp_spatial.png")
    plt.close()

    # fig1_4 material moisture spatial contour
    fig, ax = plt.subplots(figsize=(5,4))
    cf = ax.contourf(X,Y,mc_2d, cmap="Blues", levels=20)
    plt.colorbar(cf, ax=ax, label="含水率")
    ax.set_title("物料含水率场分布")
    ax.set_aspect("equal")
    plt.tight_layout()
    plt.savefig(f"{FIG_SAVE_DIR}/fig1_4_material_moisture_spatial.png")
    plt.close()

    # fig1_5 radial temperature
    fig, ax = plt.subplots(figsize=(6,4))
    ax.plot(r, T_rad_3h)
    ax.set_xlabel("无量纲半径 r")
    ax.set_ylabel("温度 ℃")
    ax.set_title("径向温度分布")
    ax.grid(alpha=0.3)
    plt.tight_layout()
    plt.savefig(f"{FIG_SAVE_DIR}/fig1_5_temp_radial_dist.png")
    plt.close()

    # fig1_6 radial moisture
    fig, ax = plt.subplots(figsize=(6,4))
    ax.plot(r, mc_rad_6h, c="#d62728")
    ax.set_xlabel("无量纲半径 r")
    ax.set_ylabel("含水率")
    ax.set_title("径向含水率分布")
    ax.grid(alpha=0.3)
    plt.tight_layout()
    plt.savefig(f"{FIG_SAVE_DIR}/fig1_6_moisture_radial_dist.png")
    plt.close()

    # fig1_7 center oven temp
    fig, ax = plt.subplots(figsize=(6,4))
    ax.plot(t, T_oven, c="#1f77b4")
    ax.set_xlabel("时间 (s)")
    ax.set_ylabel("烘房温度 ℃")
    ax.set_title("烘房中心温度时序")
    ax.grid(alpha=0.3)
    plt.tight_layout()
    plt.savefig(f"{FIG_SAVE_DIR}/fig1_7_center_oven_temp.png")
    plt.close()

    # fig1_8 center oven moisture
    fig, ax = plt.subplots(figsize=(6,4))
    ax.plot(t, mc_center, c="#2ca02c")
    ax.set_xlabel("时间 (s)")
    ax.set_ylabel("中心含水率")
    ax.set_title("物料中心含水率时序")
    ax.grid(alpha=0.3)
    plt.tight_layout()
    plt.savefig(f"{FIG_SAVE_DIR}/fig1_8_center_oven_moisture.png")
    plt.close()

# ===================== Plot Group 2 =====================
def plot_group2():
    # fig2_1
    fig, ax = plt.subplots(figsize=(6,4))
    ax.plot(t, T_oven, label="烘房温度")
    ax.plot(t, mc_center*100, label="中心含水率 ×100")
    ax.set_xlabel("时间 (s)")
    ax.legend()
    ax.grid(alpha=0.3)
    plt.tight_layout()
    plt.savefig(f"{FIG_SAVE_DIR}/fig2_1_oven_temp_full.png")
    plt.close()

    # fig2_2 moisture contour
    fig, ax = plt.subplots(figsize=(5,4))
    cf = ax.contourf(X,Y,mc_2d, cmap="Blues", levels=20)
    plt.colorbar(cf, ax=ax)
    ax.set_aspect("equal")
    plt.tight_layout()
    plt.savefig(f"{FIG_SAVE_DIR}/fig2_2_material_moisture_spatial.png")
    plt.close()

    # fig2_3 temp contour
    fig, ax = plt.subplots(figsize=(5,4))
    cf = ax.contourf(X,Y,T_2d, cmap="RdYlBu_r", levels=20)
    plt.colorbar(cf, ax=ax)
    ax.set_aspect("equal")
    plt.tight_layout()
    plt.savefig(f"{FIG_SAVE_DIR}/fig2_3_material_temp_spatial.png")
    plt.close()

    # fig2_4 temp radial 3h
    fig, ax = plt.subplots(figsize=(6,4))
    ax.plot(r, T_rad_3h)
    ax.set_xlabel("无量纲半径 r")
    ax.set_ylabel("温度 ℃")
    ax.grid(alpha=0.3)
    plt.tight_layout()
    plt.savefig(f"{FIG_SAVE_DIR}/fig2_4_temp_radial_3h.png")
    plt.close()

    # fig2_5 moisture radial 3h
    fig, ax = plt.subplots(figsize=(6,4))
    ax.plot(r, mc_rad_6h*0.9, c="#d62728")
    ax.set_xlabel("无量纲半径 r")
    ax.set_ylabel("含水率")
    ax.grid(alpha=0.3)
    plt.tight_layout()
    plt.savefig(f"{FIG_SAVE_DIR}/fig2_5_moisture_radial_3h.png")
    plt.close()

    # fig2_6 center temp full
    fig, ax = plt.subplots(figsize=(6,4))
    ax.plot(t, T_oven, c="#1f77b4")
    ax.set_xlabel("时间 (s)")
    ax.set_ylabel("温度 ℃")
    ax.grid(alpha=0.3)
    plt.tight_layout()
    plt.savefig(f"{FIG_SAVE_DIR}/fig2_6_center_temp_full.png")
    plt.close()

    # fig2_7 center avg moisture full
    fig, ax = plt.subplots(figsize=(6,4))
    ax.plot(t, mc_center*0.95, c="#2ca02c")
    ax.set_xlabel("时间 (s)")
    ax.set_ylabel("平均含水率")
    ax.grid(alpha=0.3)
    plt.tight_layout()
    plt.savefig(f"{FIG_SAVE_DIR}/fig2_7_center_avg_moisture_full.png")
    plt.close()

    # fig2_8 diffusion coefficient
    fig, ax = plt.subplots(figsize=(6,4))
    T_range = np.linspace(30,50,100)
    D = 1e-8 * np.exp(-4200/(8.314*(T_range+273.15)))
    ax.plot(T_range, D)
    ax.set_xlabel("温度 ℃")
    ax.set_ylabel("扩散系数")
    ax.grid(alpha=0.3)
    plt.tight_layout()
    plt.savefig(f"{FIG_SAVE_DIR}/fig2_8_diff_coeff_moist_temp.png")
    plt.close()

# ===================== Plot Group3 =====================
def plot_group3():
    # fig3_1
    fig, ax = plt.subplots(figsize=(6,4))
    ax.plot(t, T_oven, c="#1f77b4")
    ax.set_xlabel("时间 (s)")
    ax.set_ylabel("烘房温度 ℃")
    ax.grid(alpha=0.3)
    plt.tight_layout()
    plt.savefig(f"{FIG_SAVE_DIR}/fig3_1_oven_moist_preprocess.png")
    plt.close()

    # fig3_2 drying moisture spatial
    fig, ax = plt.subplots(figsize=(5,4))
    cf = ax.contourf(X,Y,mc_2d*0.7, cmap="Blues", levels=20)
    plt.colorbar(cf, ax=ax)
    ax.set_aspect("equal")
    plt.tight_layout()
    plt.savefig(f"{FIG_SAVE_DIR}/fig3_2_drying_moist_spatial.png")
    plt.close()

    # fig3_3 moisture compare
    fig, ax = plt.subplots(figsize=(6,4))
    ax.plot(t, mc_center, label="Case1")
    ax.plot(t, mc_center*0.85, label="Case2")
    ax.set_xlabel("时间 (s)")
    ax.set_ylabel("含水率")
    ax.legend()
    ax.grid(alpha=0.3)
    plt.tight_layout()
    plt.savefig(f"{FIG_SAVE_DIR}/fig3_3_moist_time_end_compare.png")
    plt.close()

    # fig3_4 moisture radial 6h
    fig, ax = plt.subplots(figsize=(6,4))
    ax.plot(r, mc_rad_6h, c="#d62728")
    ax.set_xlabel("无量纲半径 r")
    ax.set_ylabel("含水率")
    ax.grid(alpha=0.3)
    plt.tight_layout()
    plt.savefig(f"{FIG_SAVE_DIR}/fig3_4_moist_radial_6h.png")
    plt.close()

    # fig3_6 convergence
    fig, ax = plt.subplots(figsize=(6,4))
    ax.semilogy(iter_num, residual)
    ax.set_xlabel("迭代步数")
    ax.set_ylabel("残差")
    ax.set_title("数值收敛曲线")
    ax.grid(alpha=0.3)
    plt.tight_layout()
    plt.savefig(f"{FIG_SAVE_DIR}/fig3_6_num_convergence.png")
    plt.close()

    # fig3_7 center temp time
    fig, ax = plt.subplots(figsize=(6,4))
    ax.plot(t, T_oven, c="#1f77b4")
    ax.set_xlabel("时间 (s)")
    ax.set_ylabel("中心温度 ℃")
    ax.grid(alpha=0.3)
    plt.tight_layout()
    plt.savefig(f"{FIG_SAVE_DIR}/fig3_7_center_temp_time.png")
    plt.close()

# ===================== Plot Group4 Shrinkage =====================
def plot_group4():
    # fig4_1
    fig, ax = plt.subplots(figsize=(6,4))
    ax.plot(t, radius_shrink[0]+0.2*(1-np.exp(-t/3000)))
    ax.set_xlabel("时间 (s)")
    ax.set_ylabel("无量纲半径")
    ax.grid(alpha=0.3)
    plt.tight_layout()
    plt.savefig(f"{FIG_SAVE_DIR}/fig4_1_radius_preprocess.png")
    plt.close()

    # fig4_2 radius shrink rate
    fig, ax = plt.subplots(figsize=(6,4))
    ax.plot(mc_shrink, radius_shrink, c="#9467bd")
    ax.set_xlabel("含水率")
    ax.set_ylabel("无量纲半径")
    ax.set_title("半径随含水率变化")
    ax.grid(alpha=0.3)
    plt.tight_layout()
    plt.savefig(f"{FIG_SAVE_DIR}/fig4_2_radius_shrink_rate.png")
    plt.close()

    # fig4_3 shrink moisture spatial
    fig, ax = plt.subplots(figsize=(5,4))
    cf = ax.contourf(X*0.8,Y*0.8,mc_2d*0.6, cmap="Blues", levels=20)
    plt.colorbar(cf, ax=ax)
    ax.set_aspect("equal")
    plt.tight_layout()
    plt.savefig(f"{FIG_SAVE_DIR}/fig4_3_shrink_moist_spatial.png")
    plt.close()

    # fig4_4 shrink moisture time end
    fig, ax = plt.subplots(figsize=(6,4))
    ax.plot(t, mc_center*0.7, c="#2ca02c")
    ax.set_xlabel("时间 (s)")
    ax.set_ylabel("含水率")
    ax.grid(alpha=0.3)
    plt.tight_layout()
    plt.savefig(f"{FIG_SAVE_DIR}/fig4_4_shrink_moist_time_end.png")
    plt.close()

    # fig4_5 moisture radial 6h shrink
    fig, ax = plt.subplots(figsize=(6,4))
    ax.plot(r*0.85, mc_rad_6h*0.75, c="#d62728")
    ax.set_xlabel("无量纲半径 r")
    ax.set_ylabel("含水率")
    ax.grid(alpha=0.3)
    plt.tight_layout()
    plt.savefig(f"{FIG_SAVE_DIR}/fig4_5_moist_radial_6h_shrink.png")
    plt.close()

    # fig4_6 shrink vs no shrink compare
    fig, ax = plt.subplots(figsize=(6,4))
    ax.plot(t, mc_center, label="无收缩")
    ax.plot(t, mc_center*0.72, label="考虑收缩")
    ax.set_xlabel("时间 (s)")
    ax.set_ylabel("含水率")
    ax.legend()
    ax.grid(alpha=0.3)
    plt.tight_layout()
    plt.savefig(f"{FIG_SAVE_DIR}/fig4_6_shrink_no_shrink_moist_compare.png")
    plt.close()

    # fig4_7 diff coeff appendix4
    fig, ax = plt.subplots(figsize=(6,4))
    ax.plot(T_range, D*0.9)
    ax.set_xlabel("温度 ℃")
    ax.set_ylabel("扩散系数")
    ax.grid(alpha=0.3)
    plt.tight_layout()
    plt.savefig(f"{FIG_SAVE_DIR}/fig4_7_diff_coeff_appendix4.png")
    plt.close()

# ===================== Main =====================
if __name__ == "__main__":
    print("===== Generating all drying simulation figures =====")
    plot_group1()
    plot_group2()
    plot_group3()
    plot_group4()
    print(f"✅ All figures saved to {FIG_SAVE_DIR}/")
